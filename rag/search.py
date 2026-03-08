import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

index = faiss.read_index("index/faiss.index")

chunks = pickle.load(open("index/metadata.pkl", "rb"))


def search(query, k=5):

    q = model.encode([query], normalize_embeddings=True)

    scores, ids = index.search(q, k)

    return [chunks[i]["content"] for i in ids[0]]


if __name__ == "__main__":

    results = search("modern SaaS landing page")

    for r in results:
        print("\n---\n")
        print(r)