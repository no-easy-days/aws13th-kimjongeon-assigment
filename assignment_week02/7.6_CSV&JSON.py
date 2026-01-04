import csv

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이", "도시", "직업"])
    writer.writerow(["홍길동",25,"서울","개발자"])
    writer.writerow(["김철수",30,"부산","디자이너"])
    writer.writerow(["이영희",28,"대전","마케터"])
    writer.writerow(["박지민",35,"인천","데이터분석가"])


"""
1. users.csv 파일을 읽어서 모든 사용자의 이름과 직업을 출력하세요.
홍길동 - 개발자
김철수 - 디자이너
이영희 - 마케터
박지민 - 데이터분석가
"""
with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['이름']} -  {row['직업']}")


"""
2. users.csv에서 나이가 30세 이상인 사용자만 출력하세요.
김철수 (30세)
박지민 (35세)
"""
with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row['나이']) >= 30:
            print(f"{row['이름']} ({row['나이']}세)")

"""
3. 다음 학생 데이터를 students.csv 파일로 저장하세요.
students = [
{'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
{'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
{'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]
"""
students = [
{'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
{'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
{'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]

with open('students.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['학번', '이름', '학과']  # 컬럼 순서 지정
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)


"""
4. `config.json` 파일을 읽어서 다음 정보를 출력하세요.
- 앱 이름
- 버전
- 데이터베이스 호스트
"""
import json
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": False,
    "database": {
        "host": "localhost",
        "port": 3306,
        "name": "mydb"
    },
    "features": ["login", "dashboard", "settings"]
}
#파일 쓰기
with open('config.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

#파일 읽기
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
print(f"앱 이름: {config['app_name']}")
print(f"버전: {config['version']}")
print(f"DB 호스트: {config['database']['host']}")


"""
5. `config.json`을 읽어서 다음 변경 후 `config_updated.json`으로 저장하세요.

1. `debug`를 `true`로 변경
2. `features` 리스트에 `"notifications"` 추가
"""
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

config['debug'] = True
config['features'].append('notifications')

with open('config_updated.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)


"""
6. users.csv를 읽어서 users.json으로 변환하세요.
"""
def csv_to_json(csv_file, json_file):
    """CSV를 JSON으로 변환"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

csv_to_json('users.csv', 'users.json')

"""
7. 다음 JSON 로그 데이터에서 "ERROR" 레벨의 로그만 추출하여 errors.json으로 저장하세요.
"""
logs = [
    {"timestamp": "2025-01-01 10:00:00", "level": "INFO", "message": "서버 시작"},
    {"timestamp": "2025-01-01 10:05:00", "level": "ERROR", "message": "DB 연결 실패"},
    {"timestamp": "2025-01-01 10:10:00", "level": "INFO", "message": "재연결 시도"},
    {"timestamp": "2025-01-01 10:15:00", "level": "ERROR", "message": "타임아웃 발생"},
    {"timestamp": "2025-01-01 10:20:00", "level": "INFO", "message": "정상 복구"}
]

#파일 쓰기
with open('logs.json', 'w', encoding='utf-8') as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

#파일 읽기
with open('logs.json', 'r', encoding='utf-8') as f:
    logs = json.load(f)

errors = [log for log in logs if log['level'] == 'ERROR']

with open('errors.json', 'w', encoding='utf-8') as f:
    json.dump(errors, f, ensure_ascii=False, indent=2)




