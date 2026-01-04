"""
1. 텍스트 파일을 읽어 다음 통계를 출력하는 프로그램을 작성하세요.
**출력 내용**
- 전체 줄 수
- 전체 단어 수
- 전체 문자 수
- 가장 긴 줄의 길이
"""
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write("Hello world!\n")
    f.write("Nice to meet you!\n")
    f.write("Happy new year")

with open('text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print(f"전체 줄 수: {len(lines)}")
    print(f"전체 단어 수: {sum(len(i.split()) for i in lines)}")
    print(f"전체 문자 수: {sum(len(i) for i in lines)}")
    print(f"가장 긴 줄의 길이: {max(len(i) for i in lines)}")

"""
2. 날짜별로 일기를 저장하고 읽을 수 있는 프로그램을 작성하세요.
**기능**
1. 오늘 일기 쓰기 (파일명: `diary_2025-12-28.txt`)
2. 특정 날짜 일기 읽기
3. 모든 일기 목록 보기
"""
from datetime import datetime
import os

class DiaryManager:
    def __init__(self, folder="diary"):
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)

    def write_diary(self, content, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")

        filename = f"{self.folder}/diary_{date}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"일기가 저장되었습니다: {filename}")

    def read_diary(self, date):
        filename = f"{self.folder}/diary_{date}.txt"

        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return f"{date} 날짜의 일기가 없습니다."

    def list_diaries(self):
        files = [
            file for file in os.listdir(self.folder)
            if file.startswith("diary_") and file.endswith(".txt")
        ]
        return sorted(files)
diary = DiaryManager()
diary.write_diary("Happy new year!")

today = datetime.now().strftime("%Y-%m-%d")
print("\n[오늘 일기]")
print(diary.read_diary(today))

print("\n[일기 목록]")
for file in diary.list_diaries():
    print("-", file)

"""
3. 원본 파일을 복사하는 프로그램을 작성하세요.

**요구사항**
- 텍스트 파일과 바이너리 파일 모두 지원
- 파일이 없으면 적절한 에러 메시지 출력
- 복사 완료 후 파일 크기 비교
**힌트**: 큰 파일은 청크 단위(4096 bytes)로 복사
"""
import os

CHUNK_SIZE = 4096

def copy_file(src_path: str, dst_path: str) -> None:
    if not os.path.isfile(src_path):
        print(f"[에러] 원본 파일이 존재하지 않습니다: {src_path}")
        return

    try:
        with open(src_path, "rb") as src_file:
            with open(dst_path, "wb") as dst_file:
                while True:
                    chunk = src_file.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    dst_file.write(chunk)
        src_size = os.path.getsize(src_path)
        dst_size = os.path.getsize(dst_path)

        print("복사가 끝났습니다!")
        print(f"원본 크기: {src_size} bytes")
        print(f"복사본 크기: {dst_size} bytes")

        if src_size == dst_size:
            print("크기가 동일합니다. 복사가 정상적으로 완료되었습니다.")
        else:
            print("크기가 다릅니다. 복사 중 문제가 있었을 수 있습니다.")

    except PermissionError:
        print("권한이 없습니다. 파일 접근 권한을 확인하세요.")
    except OSError as e:
        print(f"파일 처리 중 문제가 발생했습니다: {e}")


if __name__ == "__main__":
    src = input("원본 파일 경로를 입력하세요: ").strip()
    dst = input("복사할 파일 경로를 입력하세요: ").strip()
    copy_file(src, dst)

