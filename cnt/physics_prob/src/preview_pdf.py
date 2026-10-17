import fitz
import os

base = r"C:\Users\ForcePC\source\ai\ai4physics\cnt\physics_prob"
pdf_path = os.path.join(base, "paper", "paper.pdf")
out_dir = os.path.join(base, "paper")

doc = fitz.open(pdf_path)
print(f"Pages: {doc.page_count}")
for i in range(min(2, doc.page_count)):
    page = doc[i]
    pix = page.get_pixmap(dpi=150)
    out_path = os.path.join(out_dir, f"preview_page_{i+1}.png")
    pix.save(out_path)
    print(f"Page {i+1} saved to {out_path}")