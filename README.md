# AI Studio TXT Converter

AI Studio 대화 JSON을 사람이 읽기 쉬운 TXT로 변환하고, TXT 파일을 합치거나 PDF 텍스트를 간단히 추출하기 위한 작은 Python 스크립트 모음입니다.

## 파일 구성

| 파일 | 기능 |
| --- | --- |
| `converter.py` | AI Studio 대화 JSON 파일을 `[User]`, `[AI]` 태그가 붙은 TXT 파일로 변환합니다. |
| `txt_merger.py` | TXT 파일 2개를 선택해 하나의 `merged.txt` 파일로 합칩니다. |
| `pdf_reader.py` | 코드에 지정된 PDF 파일에서 텍스트를 추출해 콘솔에 출력합니다. |

## 요구 사항

- Python 3
- `tkinter`
  - `converter.py`, `txt_merger.py`에서 파일 선택 창을 띄우는 데 사용합니다.
  - 일반적인 Windows Python 설치에는 기본 포함되어 있습니다.
- `PyPDF2`
  - `pdf_reader.py`에서 PDF를 읽는 데 사용합니다.

`PyPDF2`가 설치되어 있지 않다면 다음 명령으로 설치합니다.

```powershell
python -m pip install PyPDF2
```

## 사용 방법

### 1. AI Studio JSON을 TXT로 변환하기

```powershell
python converter.py
```

실행하면 JSON 파일 선택 창이 열립니다. 여러 파일을 한 번에 선택할 수 있습니다.

`converter.py`는 다음 두 가지 JSON 구조를 지원합니다.

- `messages`
- `chunkedPrompt.chunks`

각 항목의 `role` 값이 `user`이면 `[User]`, `model`이면 `[AI]` 태그를 붙입니다. 그 외 role은 변환 대상에서 제외합니다.

출력 파일은 원본 JSON 파일과 같은 폴더에 저장됩니다.

예시:

```text
example.json -> example_converted.txt
```

저장 인코딩은 `utf-8-sig`입니다.

### 2. TXT 파일 2개 합치기

```powershell
python txt_merger.py
```

실행하면 첫 번째 TXT 파일과 두 번째 TXT 파일을 차례로 선택합니다.

동작 방식:

- 먼저 `utf-8`로 파일을 읽습니다.
- `utf-8` 읽기에 실패하면 `cp949`로 다시 읽습니다.
- 두 파일의 앞뒤 공백을 제거한 뒤, 중간에 빈 줄 하나를 넣어 합칩니다.
- 결과는 첫 번째 파일이 있는 폴더에 `merged.txt`로 저장합니다.
- 저장 인코딩은 `utf-8-sig`입니다.

주의: 같은 폴더에 기존 `merged.txt`가 있으면 덮어씁니다.

### 3. PDF 텍스트 출력하기

```powershell
python pdf_reader.py
```

`pdf_reader.py`는 현재 다음 경로의 PDF를 읽도록 코드에 고정되어 있습니다.

```text
C:\Users\yount\Downloads\flutter_app_ffmpeg_issues.pdf
```

동작 방식:

- `PyPDF2.PdfReader`로 PDF를 엽니다.
- 모든 페이지를 순회하며 `extract_text()` 결과를 이어 붙입니다.
- 추출한 텍스트를 콘솔에 출력합니다.

현재 버전은 PDF 파일 선택 창을 띄우지 않고, 결과를 TXT 파일로 저장하지도 않습니다. 다른 PDF를 읽으려면 `pdf_dir` 값을 직접 수정해야 합니다.

## 출력 파일 정리

| 스크립트 | 출력 위치 | 출력 파일명 |
| --- | --- | --- |
| `converter.py` | 원본 JSON과 같은 폴더 | `{원본파일명}_converted.txt` |
| `txt_merger.py` | 첫 번째 TXT 파일과 같은 폴더 | `merged.txt` |
| `pdf_reader.py` | 파일 저장 없음 | 콘솔 출력만 수행 |

## 개선하면 좋은 점

- `pdf_reader.py`도 `tkinter` 파일 선택 창을 사용하도록 변경
- PDF 추출 결과를 TXT 파일로 저장하는 기능 추가
- `txt_merger.py`에서 저장 파일명을 사용자가 직접 고를 수 있게 변경
- `converter.py`에서 사용자 태그와 AI 태그를 실행 옵션으로 지정하는 기능 추가
