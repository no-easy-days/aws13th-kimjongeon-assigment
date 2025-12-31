"""
1. 학생 정보를 관리하는 `Student` 클래스를 만드세요.
**요구사항**
- 속성: `name` (이름), `student_id` (학번), `grade` (학년)
- 메서드: `introduce()` - "안녕하세요, {학년}학년 {이름}입니다. (학번: {학번})" 출력
"""


class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def introduce(self):
        print(f"안녕하세요, {self.grade}학년 {self.name}입니다. (학번: {self.student_id})")


kim = Student("김철수", "2024001", 1)
kim.introduce()

'''
2. 은행 계좌를 관리하는 `BankAccount` 클래스를 만드세요.
**요구사항**
- 속성: `owner` (예금주), `balance` (잔액, 기본값 0)
- 메서드
    - `deposit(amount)` - 입금 (잔액 증가)
    - `withdraw(amount)` - 출금 (잔액 감소, 잔액 부족 시 "잔액이 부족합니다" 출력)
    - `get_balance()` - 현재 잔액 반환
'''


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다.")
        self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("홍길동")
account.deposit(10000)
account.withdraw(3000)
print(account.get_balance())  # 7000
account.withdraw(10000)  # 잔액이 부족합니다

"""
3. 리스트 속성 관리하기
할 일 목록을 관리하는 `TodoList` 클래스를 만드세요.
**요구사항**
- 속성: `tasks` (할 일 목록, 빈 리스트로 시작)
- 메서드
    - `add_task(task)` - 할 일 추가
    - `complete_task(task)` - 할 일 완료 (목록에서 제거)
    - `show_tasks()` - 현재 할 일 목록 출력
"""


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, task):
        self.tasks.remove(task)
        print(f"{task}이(가) 완료되었습니다.")

    def show_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")


my_todo = TodoList()
my_todo.add_task("Python 공부")
my_todo.add_task("Git 연습")
my_todo.show_tasks()
# 출력:
# 1. Python 공부
# 2. Git 연습
my_todo.complete_task("Python 공부")
my_todo.show_tasks()
# 출력:
# 1. Git 연습

"""
4. `dataclass`를 사용하여 서버 설정 정보를 저장하는 클래스를 만드세요.
**요구사항**
- 클래스명: `DatabaseConfig`
- 속성
    - `host`: str (필수)
    - `port`: int (필수)
    - `username`: str (필수)
    - `password`: str (필수)
    - `database`: str (필수)
    - `timeout`: int (기본값: 30)
    - `pool_size`: int (기본값: 5)
"""
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    host: str
    port: int
    username: str
    password: str
    database: str
    timeout: int = 30
    pool_size: int = 5


config = DatabaseConfig(
    host="[localhost](http://localhost)",
    port=3306,
    username="admin",
    password="secret123",
    database="myapp"
)
print(config)

"""
Challenge Prob. 
여러 EC2 인스턴스를 관리하는 시스템을 만드세요.
**요구사항**
`EC2Instance` 클래스
- 속성: `instance_id`, `name`, `status` (기본값: "stopped")
- 메서드: `start()`, `stop()`
`EC2Manager` 클래스
- 속성: `instances` (인스턴스 목록)
- 메서드
    - `add_instance(instance)` - 인스턴스 추가
    - `start_all()` - 모든 인스턴스 시작
    - `stop_all()` - 모든 인스턴스 중지
    - `get_running_count()` - 실행 중인 인스턴스 개수 반환
"""


class EC2Instance:
    def __init__(self, instance_id, name):
        self.instance_id = instance_id
        self.name = name
        self.status = "stopped"

    def start(self):
        self.status = "start"

    def stop(self):
        self.status = "stopped"


class EC2Manager:
    def __init__(self):
        self.instances = []

    def add_instance(self, instance):
        self.instances.append(instance)

    def start_all(self):
        for instance in self.instances:
            instance.start()

    def stop_all(self):
        for instance in self.instances:
            instance.stop()

    def get_running_count(self):
        cnt = 0
        for instance in self.instances:
            if instance.status == "start":
                cnt += 1
        return cnt

# 인스턴스 생성
web = EC2Instance("i-001", "web-server")
db = EC2Instance("i-002", "db-server")
cache = EC2Instance("i-003", "cache-server")

# 매니저에 등록
manager = EC2Manager()
manager.add_instance(web)
manager.add_instance(db)
manager.add_instance(cache)

# 모두 시작
manager.start_all()
print(manager.get_running_count())  # 3

# 일부 중지
db.stop()
print(manager.get_running_count())  # 2
