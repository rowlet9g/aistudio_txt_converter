# AI Studio TXT Converter

AI Studio 대화 JSON을 TXT로 변환하고, TXT 파일 병합과 PDF 텍스트 추출을 GUI 파일 선택 방식으로 처리하는 Python 스크립트 모음입니다.

## 파일 구성

| 파일 | 기능 |
| --- | --- |
| `converter.py` | AI Studio 대화 JSON 파일을 `[User]`, `[AI]` 같은 태그가 붙은 TXT 파일로 변환합니다. |
| `txt_merger.py` | TXT 파일 2개를 선택해 하나의 TXT 파일로 합칩니다. |
| `pdf_reader.py` | PDF 파일을 선택해 텍스트를 추출하고 TXT 파일로 저장합니다. |
| `requirements.txt` | 외부 Python 패키지 의존성을 기록합니다. |

## 설치

Python 3이 필요합니다. PDF 텍스트 추출에는 `PyPDF2`가 필요합니다.

```powershell
python -m pip install -r requirements.txt
```

`converter.py`, `txt_merger.py`, `pdf_reader.py`는 모두 `tkinter` 파일 선택 창을 사용합니다. 일반적인 Windows Python 설치에는 `tkinter`가 기본 포함되어 있습니다.

## 사용 방법

### 1. AI Studio JSON을 TXT로 변환하기

```powershell
python converter.py
```

실행 흐름:

1. 사용자 태그 입력 창이 열립니다. 기본값은 `[User]`입니다.
2. AI 태그 입력 창이 열립니다. 기본값은 `[AI]`입니다.
3. 변환할 JSON 파일을 선택합니다. 여러 파일을 한 번에 선택할 수 있습니다.
4. 각 JSON 파일과 같은 폴더에 `{원본파일명}_converted.txt`가 저장됩니다.

지원하는 JSON 구조:

- `messages`
- `chunkedPrompt.chunks`

각 항목의 `role` 값이 `user`이면 사용자 태그를 붙이고, `model`이면 AI 태그를 붙입니다. 그 외 role은 변환하지 않습니다.

출력은 `utf-8-sig` 인코딩으로 저장합니다.

### 2. TXT 파일 2개 합치기

```powershell
python txt_merger.py
```

실행 흐름:

1. 첫 번째 TXT 파일을 선택합니다.
2. 두 번째 TXT 파일을 선택합니다.
3. 저장할 파일명과 위치를 선택합니다. 기본 파일명은 `merged.txt`입니다.
4. 두 파일의 내용이 합쳐진 TXT 파일이 저장됩니다.

동작 방식:

- 먼저 `utf-8`로 파일을 읽습니다.
- `utf-8` 읽기에 실패하면 `cp949`로 다시 읽습니다.
- 두 파일의 앞뒤 공백을 제거한 뒤, 중간에 빈 줄 하나를 넣어 합칩니다.
- 출력은 `utf-8-sig` 인코딩으로 저장합니다.

### 3. PDF 텍스트 추출하기

```powershell
python pdf_reader.py
```

실행 흐름:

1. PDF 파일을 선택합니다.
2. 저장할 TXT 파일명과 위치를 선택합니다. 기본 파일명은 `{PDF파일명}_extracted.txt`입니다.
3. PDF의 각 페이지에서 텍스트를 추출해 TXT 파일로 저장합니다.

주의 사항:

- PDF가 스캔 이미지로만 구성되어 있으면 `PyPDF2`가 텍스트를 추출하지 못할 수 있습니다.
- 텍스트가 없는 페이지는 콘솔에 `no extractable text` 메시지를 출력하고 건너뜁니다.
- 출력은 `utf-8-sig` 인코딩으로 저장합니다.

## 출력 파일 정리

| 스크립트 | 기본 출력 위치 | 기본 출력 파일명 |
| --- | --- | --- |
| `converter.py` | 원본 JSON과 같은 폴더 | `{원본파일명}_converted.txt` |
| `txt_merger.py` | 사용자가 선택 | `merged.txt` |
| `pdf_reader.py` | 사용자가 선택 | `{PDF파일명}_extracted.txt` |

## 현재 한계

- `converter.py`는 JSON 파일마다 별도 저장 파일명을 선택하지 않고, 정해진 규칙으로 자동 저장합니다.
- `txt_merger.py`는 한 번에 TXT 파일 2개만 합칩니다.
- `pdf_reader.py`는 OCR 기능이 없어서 이미지 기반 PDF의 글자는 추출하지 못합니다.
