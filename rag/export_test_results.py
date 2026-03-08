import pickle
import faiss
import json
from sentence_transformers import SentenceTransformer

BUNDLE_PATH = "uupm_rag_bundle.pkl"

print("Loading bundle...")

bundle = pickle.load(open(BUNDLE_PATH, "rb"))

index = faiss.deserialize_index(bundle["index"])
metadata = bundle["metadata"]
model = SentenceTransformer(bundle["embedding_model"])


def search(query, k=3):
    q = model.encode([query], normalize_embeddings=True)
    scores, ids = index.search(q, k)
    return [metadata[i]["content"] for i in ids[0]]


# 10 verification queries
queries = [
    "modern SaaS landing page",
    "fintech dashboard UI",
    "brutalist portfolio design",
    "responsive navigation bar",
    "hero section design",
    "pricing table layout",
    "testimonial cards UI",
    "mobile accessibility rules",
    "dark mode interface design",
    "startup landing page structure"
]

results = []

for q in queries:

    retrieved = search(q)

    results.append({
        "query": q,
        "results": retrieved
    })


with open("rag_test_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nTest results exported → rag_test_results.json")