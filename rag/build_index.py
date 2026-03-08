import json
import faiss
import numpy as np
import pickle

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def load_chunks():
    return json.load(open("../data/uupm_chunks.json"))


def embed_texts(texts):

    embeddings = model.encode(texts, normalize_embeddings=True)

    return np.array(embeddings)


if __name__ == "__main__":

    chunks = load_chunks()

    texts = [c["content"] for c in chunks]

    embeddings = embed_texts(texts)

    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)

    index.add(embeddings)

    faiss.write_index(index, "index/faiss.index")

    pickle.dump(chunks, open("index/metadata.pkl", "wb"))

    print("FAISS index built")