import pickle
import faiss
from pathlib import Path

INDEX_PATH = "index/faiss.index"
META_PATH = "index/metadata.pkl"
OUTPUT_PATH = "uupm_rag_bundle.pkl"

def export_bundle():

    index = faiss.read_index(INDEX_PATH)

    metadata = pickle.load(open(META_PATH, "rb"))

    bundle = {
        "index": faiss.serialize_index(index),
        "metadata": metadata,
        "embedding_model": "BAAI/bge-small-en-v1.5",
        "version": "1.0"
    }

    with open(OUTPUT_PATH, "wb") as f:
        pickle.dump(bundle, f)

    print(f"Bundle saved → {OUTPUT_PATH}")


if __name__ == "__main__":
    export_bundle()