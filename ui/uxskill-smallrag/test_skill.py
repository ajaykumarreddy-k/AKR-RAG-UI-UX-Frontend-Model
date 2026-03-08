from load_skill import UXSkillRAG

rag = UXSkillRAG()

results = rag.search("modern SaaS landing page")

for r in results:
    print("\n---\n")
    print(r)