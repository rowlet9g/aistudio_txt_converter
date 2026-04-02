import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

# ---- 1. GUI 루트 창 숨기기 ----
root = tk.Tk()
root.withdraw()

print("Merge two txt files to one.\n")

# ---- 2. 파일 선택 ----
print("Choose the first file.")
file1_path = filedialog.askopenfilename(
    title="First",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)

if not file1_path:
    print("First file is not selected. Exit the process.")
    exit()

print("Choose the second file.")
file2_path = filedialog.askopenfilename(
    title="Second",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)

if not file2_path:
    print("Second file is not selected. Exit the process.")
    exit()

# ---- 3. 파일 읽기 헬퍼 함수 (자동 인코딩 처리) ----
def read_text_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # 윈도우 기본 인코딩(ANSI) 파일일 경우 cp949로 재시도
        with open(filepath, 'r', encoding='cp949') as f:
            return f.read()

# ---- 4. 실제 변환 및 저장 ----
try:
    # 내용 읽기
    content1 = read_text_file(file1_path)
    content2 = read_text_file(file2_path)

    # 두 파일 내용 합치기 (중간에 줄바꿈 추가)
    merged_content = content1.strip() + '\n\n' + content2.strip() + '\n'

    # 저장할 경로 지정 (첫 번째 파일이 있는 폴더에 저장)
    parent_dir = Path(file1_path).parent
    merged_filename = parent_dir / 'merged.txt'

    # 합쳐진 파일 쓰기 (한글 깨짐 방지를 위해 utf-8-sig 사용)
    with open(merged_filename, 'w', encoding='utf-8-sig') as f:
        f.write(merged_content)

    print(f"\n'{Path(file1_path).name}'와 '{Path(file2_path).name}' file merged successfully.")
    print(f"Saved in: {merged_filename}")

except Exception as e:
    print(f"\nError while processing! : {e}")