'''
1. 점수를 입력받아 등급을 출력하세요.
| 점수      | 등급 |
| 90점 이상 | A |
| 80점 이상 | B |
| 70점 이상 | C |
| 60점 이상 | D |
| 60점 미만 | F |
**추가 조건**: 점수가 0~100 범위를 벗어나면 "잘못된 입력입니다" 출력
'''
grade = int(input("점수를 입력하세요: "))
if grade > 100 or grade < 0:
    print("잘못된 입력입니다.")
elif grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

'''
2. 사용자가 원하는 단의 구구단을 출력하세요.
출력 예시:
=== 5단 ===
5 x 1 = 5
5 x 2 = 10
...
5 x 9 = 45
'''
dan = int(input("출력할 단을 입력하세요: "))
print(f"=== {dan}단 ===")
for i in range(1, 10):
    print(f"{dan} x {i} = {dan*i}")

'''3. 2부터 100까지의 모든 소수(prime number)를 출력하세요.'''
res = []
for i in range(2, 101):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        res.append(i)
print(res)
'''
해당 코드는 판별을 위해 모든 수를 순회해야하므로 효율성이 떨어진다.
break문을 활용하여 개선하는 버전을 학습하자.
'''
res = []
for i in range(2, 101):
    is_Prime = True
    '''
    i = 2일 경우 아래 for문이 실행이 되지 않으므로, is_Prime은 그대로 True임
    '''
    for j in range(2, i):
        if i % j == 0:
            is_Prime = False
            break
    if is_Prime:
        res.append(i)
print(res)

'''
4. 1~100 사이의 랜덤 숫자를 맞추는 게임을 만드세요.
  규칙:
- 정답보다 크면 "더 작은 수를 입력하세요" 출력
- 정답보다 작으면 "더 큰 수를 입력하세요" 출력
- 정답이면 "정답입니다! N번 만에 맞추셨습니다!" 출력
'''
import random

answer = random.randint(1, 100)  # 1~100 사이 랜덤 정수
num = int(input("1~100 사이의 숫자를 입력하세요: "))
cnt = 0
while True:
    if num > answer:
        num = int(input("더 작은 수를 입력하세요: "))
        cnt += 1
    elif num < answer:
        num = int(input("더 큰 수를 입력하세요: "))
        cnt += 1
    else:
        print(f"정답입니다. {cnt+1}번 만에 맞추셨습니다!")
        break







