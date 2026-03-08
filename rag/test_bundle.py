import pickle
import faiss
import random
from sentence_transformers import SentenceTransformer

BUNDLE_PATH = "uupm_rag_bundle.pkl"

print("Loading bundle...")

bundle = pickle.load(open(BUNDLE_PATH, "rb"))

index = faiss.deserialize_index(bundle["index"])
metadata = bundle["metadata"]
model = SentenceTransformer(bundle["embedding_model"])

print("Bundle loaded successfully")
print(f"Chunks loaded: {len(metadata)}")


def search(query, k=5):
    q = model.encode([query], normalize_embeddings=True)
    scores, ids = index.search(q, k)
    return [metadata[i]["content"] for i in ids[0]]


# 100 test queries
queries = [
    "modern SaaS landing page",
    "fintech dashboard UI",
    "minimal startup website",
    "brutalist portfolio design",
    "hero section layout",
    "responsive form UI",
    "pricing section layout",
    "testimonial cards design",
    "navigation bar accessibility",
    "dark mode interface",
] * 10   # repeat to reach 100 tests


success = 0
fail = 0

print("\nRunning tests...\n")

for i, q in enumerate(queries):

    try:
        results = search(q)

        if len(results) > 0:
            success += 1
        else:
            fail += 1
            print(f"Test {i+1} FAILED → empty result")

    except Exception as e:
        fail += 1
        print(f"Test {i+1} ERROR → {e}")


print("\n========== TEST SUMMARY ==========")
print(f"Total Tests: {len(queries)}")
print(f"Passed: {success}")
print(f"Failed: {fail}")

if fail == 0:
    print("ALL TESTS PASSED ✅")
else:
    print("Some tests failed ❌")