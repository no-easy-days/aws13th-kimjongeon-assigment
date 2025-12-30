'''1. 자신의 이름, 나이, 좋아하는 숫자를 각각 변수에 저장하고 출력하는 코드를 작성하세요.'''
name, age, fav_num = "Jay", 26, 7
print(f"이름: {name}, 나이: {age}, 좋아하는 숫자: {fav_num}")

'''2. first = "A"와 second = "B" 두 변수의 값을 서로 교환하세요.'''
first = "A"
second = "B"
first, second = second, first
print("first =", first, " second =", second)

'''3. balance = 10000에서 시작하여 3000을 빼고, 2를 곱한 뒤 최종 값을 출력하세요.'''
balance = 10000
print((balance - 3000) * 2)

'''
4. 아래 코드의 오류를 찾고 수정하세요
# 2nd_place = "은메달"
# user name = "홍길동"
# class = "1학년"
'''
_2nd_place = "은메달"
user_name = "홍길동"
grade = "1학년"

'''
5. 다음 값들의 자료형을 `type()` 함수로 확인하고 출력하세요
- `42`
- `3.14`
- `"Hello"`
- `True`
- `None`
'''
data = [42, 3.14, "Hello", True, None]
for d in data:
    print(f"값: {d}, 데이터 타입: {type(d)}")

''' 6. 사용자로부터 두 숫자를 입력받아 더한 값을 출력하는 프로그램을 작성하세요. '''
num1 = input("첫 번째 숫자를 입력하세요: ")
num2 = input("두 번째 숫자를 입력하세요: ")
num1 = int(num1)
num2 = int(num2)
print(f"두 수의 합: {num1 + num2}")

'''
7. 사용자의 이름, 나이, 키를 입력받아 자기소개 문장을 출력하세요.
- 내년 나이도 함께 계산하여 출력
- f-string을 사용할 것
'''
name = input("이름: ")
age = input("나이: ")
height = input("키(cm): ")
age = int(age)
print(f"저는 {name}이고 {age}살이며, 키는 {height}cm입니다. \n내년에는 {age + 1}살이 됩니다.")

'''
8. 두 숫자와 연산자를 입력받아 계산 결과를 출력하는 간단한 계산기를 만드세요.
- 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지를 모두 지원
'''
n1 = float(input("첫 번째 숫자를 입력하세요: "))
n2 = float(input("두 번째 숫자를 입력하세요: "))
op = input("연산자를 입력해주세요: ")

if op == "+":
    print(f"{n1} {op} {n2} = {n1 + n2}")
elif op == "-":
    print(f"{n1} {op} {n2} = {n1 - n2}")
elif op == "/":
    print(f"{n1} {op} {n2} = {n1 / n2}")
elif op == "*":
    print(f"{n1} {op} {n2} = {n1 * n2}")
else:
    print(f"{n1} {op} {n2} = {n1 % n2}")
