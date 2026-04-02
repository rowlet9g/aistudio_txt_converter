import json
import tkinter as tk

from pathlib import Path
from tkinter import filedialog

# ---- 1. 변환 함수 ( byte decoding 제거, dictionary 처리 ) ----
def convert_json(data: dict, tag_user='[User]', tag_ai='[AI]'):
    # AI Studio 자체 형식 두 가지 모두 지원
    chunks = data.get('messages', data.get('chunkedPrompt', {}).get('chunks', []))
    out_lines = []

    for c in chunks:
        role = c.get('role')

        if role not in ('user', 'model'):
            continue

        tag = tag_user if role == 'user' else tag_ai

        txt = c.get('text', '').replace('\\n', '\n').strip()
        out_lines.append(f'{tag}\n{txt}\n')

    return '\n'.join(out_lines)

# ---- 2. 파일 선택 window 띄우기 ( in Local GUI ) ----
root = tk.Tk()
root.withdraw() # 메인 창 숨기기

file_paths = filedialog.askopenfilenames(
    title = 'Choose Context JSON File to Convert.',
    filetypes= [('JSON Files', '*.json'), ('All Files', '*.*')]
)

if not file_paths:
    print('There are no files. Exit the script.')
    exit()

# ---- 3. Convert & Save to Local ----
for path in file_paths:
    # Read Local File
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    converted = convert_json(data)

    # Save into Same Directory as the Source File
    og_path = Path(path)
    out_name = og_path.stem + '_converted.txt'
    out_dir = og_path.parent / out_name

    # apply UTF-8 & BOM
    with open(out_dir, 'w', encoding='utf-8-sig') as out_f:
        out_f.write(converted)

    print(f'Converting finished. Saved in: {out_dir}')