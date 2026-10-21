import yaml

with open("ontology.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

cls = data["classes"]
props = data["properties"]

# Build reverse mapping: for each class, find relations where it's in domain
from collections import defaultdict
domain_of = defaultdict(list)
for pname, pinfo in props.items():
    d = pinfo["domain"]
    if isinstance(d, list):
        for dc in d:
            domain_of[dc].append((pname, pinfo["range"]))
    else:
        domain_of[d].append((pname, pinfo["range"]))

for classname, cinfo in cls.items():
    lines = [
        "---",
        "kind: класс",
        "---",
        f"# {classname}",
        "",
        cinfo["definition"],
        "",
    ]
    # Relations from this class
    rels = domain_of.get(classname, [])
    if rels:
        lines.append("Отношения от этого класса:")
        for pname, rng in rels:
            lines.append(f"- {pname}: [[{rng}]]" if not isinstance(rng, list) else f"- {pname}: {[f'[[{r}]]' for r in rng]}")
    else:
        lines.append("Отношения от этого класса: нет.")
    
    # Relations where this class is in range
    range_of = []
    for pname, pinfo in props.items():
        rng = pinfo["range"]
        if isinstance(rng, list):
            if classname in rng:
                range_of.append((pname, pinfo["domain"]))
        else:
            if rng == classname:
                range_of.append((pname, pinfo["domain"]))
    
    if range_of:
        lines.append("Атрибуты/связи входящие:")
        for pname, dom in range_of:
            lines.append(f"- {pname} ← [[{dom}]]")
    
    # Subclass link
    if cinfo["parent"]:
        lines.append("")
        lines.append("## Связи")
        lines.append(f"- подклассОт: [[{cinfo['parent']}]]")
    
    with open(f"ontology/{classname}.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

print("Done. Created", len(cls), "ontology notes.")