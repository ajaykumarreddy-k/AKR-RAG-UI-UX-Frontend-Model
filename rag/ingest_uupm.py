from pathlib import Path
import json

REPO_PATH = Path("ui-ux-pro-max-skill")

# folders we do NOT want
EXCLUDE_DIRS = [
    ".gemini",
    ".cursor",
    ".codex",
    ".agent",
    ".factory",
    ".git",
    "node_modules",
    "screenshots"
]

# filenames we want to skip
EXCLUDE_KEYWORDS = [
    "install",
    "plugin",
    "marketplace",
    "platform",
    "cli",
]

# allowed file types
ALLOWED_EXT = [".md", ".csv", ".json"]


def should_skip(file):

    # skip excluded folders
    for d in EXCLUDE_DIRS:
        if d in str(file):
            return True

    # skip install/cli docs
    for k in EXCLUDE_KEYWORDS:
        if k in file.name.lower():
            return True

    return False


def read_files():

    docs = []

    for file in REPO_PATH.rglob("*"):

        if file.suffix not in ALLOWED_EXT:
            continue

        if should_skip(file):
            continue

        try:
            text = file.read_text(encoding="utf-8")

            docs.append({
                "source": str(file),
                "content": text
            })

        except:
            pass

    return docs


def save_docs(docs):

    with open("data/raw_docs.json", "w") as f:
        json.dump(docs, f, indent=2)


if __name__ == "__main__":

    docs = read_files()

    save_docs(docs)

    print(f"Loaded {len(docs)} clean documents")