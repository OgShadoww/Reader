import pymupdf

doc = pymupdf.open("pdf/1.pdf")
out = open("output.html", "w", encoding="utf-8")

i = 0
for page in doc:
    text = page.get_text()
    paragraphs = text.split("\n")
   
    for p in paragraphs:
        out.write(f"<p class='paragraph'>{p}</p>\n")
