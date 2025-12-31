"""
1. 다음 코드의 빈칸을 채워 현재 날짜를 출력하세요.
_____ datetime
today = datetime.date.today()
print(today)
"""
import datetime
today = datetime.date.today()
print(today)

"""
2. `math` 모듈에서 `sqrt`(제곱근)와 `pow`(거듭제곱) 함수만 가져와서 사용하세요.
**요구사항**
- 16의 제곱근 출력
- 2의 10승 출력
"""
from math import sqrt, pow
print(sqrt(16))
print(pow(2, 10))

"""
3. random 모듈을 rd라는 별명으로 가져와서 1~100 사이의 랜덤 숫자를 출력하세요.
"""
import random as rd
print(rd.randint(1,100))

"""
4. 다음 상황에 맞는 pip 명령어를 작성하세요.
1. `requests` 패키지 설치
-> pip install requests
2. `pandas` 패키지 버전 2.0.0 설치
-> pip install pandas==2.0.0
3. 현재 설치된 패키지 목록 확인
-> pip list
4. 설치된 패키지를 requirements.txt로 저장
-> pip freeze > requirements.txt
"""

"""
5. 새 프로젝트 my_app을 위한 가상환경을 만들고 활성화하는 명령어를 순서대로 작성하세요. 
1. 프로젝트 폴더 생성 및 이동
-> mkdir my_app
   cd my_app

2. 가상환경 생성
-> python3 -m venv venv

3. 가상환경 활성화 (Windows)
-> source venv/bin/activate
"""

"""
6. 당신은 새 프로젝트를 시작합니다. 다음 요구사항을 만족하는 명령어들을 순서대로 작성하세요.
**요구사항**
1. `weather_app` 폴더 생성 후 이동
-> mkdir weather_app
   cd weather_app
   
2. 가상환경 생성 및 활성화
-> python3 -m venv venv
   source venv/bin/activate
   
3. `requests`와 `python-dotenv` 패키지 설치
-> pip install requests python-dotenv

4. 설치된 패키지를 requirements.txt로 저장
pip freeze > requirements.txt
"""

"""
Challenge Prob. 
팀원이 당신의 프로젝트를 클론했습니다. 
requirements.txt가 있을 때, 팀원이 동일한 환경을 구축하려면 어떤 명령어를 실행해야 할까요?

# 1. 프로젝트 폴더로 이동
-> cd weather_app

# 2. 가상환경 생성
-> python3 -m venv venv

# 3. 가상환경 활성화
-> source venv/bin/activate

# 4. requirements.txt에 있는 패키지 한번에 설치
-> pip install -r requirements.txt
"""


