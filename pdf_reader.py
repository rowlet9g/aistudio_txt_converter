from PyPDF2 import PdfReader

pdf_dir = ""

reader = PdfReader(pdf_dir)

pages = reader.pages

text = ""

for page in pages:
    sub = page.extract_text()
    text += sub

print(text)