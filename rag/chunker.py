import json

CHUNK_SIZE = 300


def chunk_text(text):

    paragraphs = text.split("\n")

    chunks = []
    current = ""

    for p in paragraphs:

        if len(current) + len(p) < CHUNK_SIZE:
            current += p + "\n"
        else:
            chunks.append(current.strip())
            current = p

    if current:
        chunks.append(current)

    return chunks


def build_chunks():

    raw = json.load(open("data/raw_docs.json"))

    chunks = []

    for doc in raw:

        parts = chunk_text(doc["content"])

        for part in parts:

            if len(part) < 50:
                continue

            chunks.append({
                "source": doc["source"],
                "content": part
            })

    return chunks


if __name__ == "__main__":

    chunks = build_chunks()

    with open("data/uupm_chunks.json", "w") as f:
        json.dump(chunks, f, indent=2)

    print(f"Created {len(chunks)} clean chunks")