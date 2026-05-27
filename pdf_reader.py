from pathlib import Path
import tkinter as tk
from tkinter import filedialog

from PyPDF2 import PdfReader


def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text_parts = []

    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if not text:
            print(f"Page {index}: no extractable text.")
            continue

        text_parts.append(text.strip())

    return "\n\n".join(text_parts).strip() + "\n"


# ---- 1. GUI 루트 창 숨기기 ----
root = tk.Tk()
root.withdraw()

print("Extract PDF text to txt file.\n")

# ---- 2. PDF 파일 선택 ----
pdf_path = filedialog.askopenfilename(
    title="Choose PDF file",
    filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
)

if not pdf_path:
    print("PDF file is not selected. Exit the process.")
    exit()

# ---- 3. 저장 경로 선택 ----
source_path = Path(pdf_path)
output_path = filedialog.asksaveasfilename(
    title="Save extracted txt file as",
    initialdir=str(source_path.parent),
    initialfile=f"{source_path.stem}_extracted.txt",
    defaultextension=".txt",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)

if not output_path:
    print("Save path is not selected. Exit the process.")
    exit()

# ---- 4. 텍스트 추출 및 저장 ----
try:
    extracted_text = extract_pdf_text(pdf_path)

    with open(output_path, "w", encoding="utf-8-sig") as f:
        f.write(extracted_text)

    print(f"PDF text extraction finished. Saved in: {output_path}")

except Exception as e:
    print(f"\nError while processing PDF! : {e}")
