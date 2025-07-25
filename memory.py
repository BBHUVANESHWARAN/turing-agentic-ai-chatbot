import os, uuid
import weaviate
from google.generativeai import configure, embed_content
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------------------------------
# 1. Connect to Weaviate
# ------------------------------------------------------------------
client = weaviate.Client(
    url=os.getenv("WEAVIATE_URL"),
    auth_client_secret=(
        weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY"))
        if os.getenv("WEAVIATE_API_KEY")
        else None
    ),
)


# ---------- schema ----------
class_name = "TuringMemory"
schema = {
    "class": class_name,
    "properties": [
        {"name": "text", "dataType": ["text"]},
    ],
    "vectorizer": "none",
}
try:
    client.schema.create_class(schema)
except weaviate.exceptions.UnexpectedStatusCodeException:
    pass  # already exists

configure(api_key=os.getenv("GOOGLE_API_KEY"))  # needed for embeddings

def embed(text: str) -> list[float]:
    return embed_content(model="models/embedding-001", content=text)["embedding"]

def save_memory(text: str):
    client.data_object.create(
        class_name=class_name,
        data_object={"text": text},
        vector=embed(text),
    )

def recall_memory(query: str, k: int = 3) -> str:
    vec = embed(query)
    res = (
        client.query
        .get(class_name, ["text"])
        .with_near_vector({"vector": vec})
        .with_limit(k)
        .do()
    )
    docs = res.get("data", {}).get("Get", {}).get(class_name, [])
    return "\n".join(d["text"] for d in docs) if docs else "No prior knowledge."