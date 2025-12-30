'''1. 두 숫자와 연산자(+, -, *, /)를 받아 계산 결과를 반환하는 함수를 만드세요.'''
def calculator(a, b, operator):
    # 여기에 코드 작성
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return a / b
    else:
        return "지원하지 않는 연산자입니다."

print(calculator(10, 5, '+'))  # 15
print(calculator(10, 5, '-'))  # 5
print(calculator(10, 5, '*'))  # 50
print(calculator(10, 5, '/'))  # 2.0
print(calculator(10, 0, '/'))  # 0으로 나눌 수 없습니다
print(calculator(10, 5, '%'))  # 지원하지 않는 연산자입니다

'''
# 2. 학생 이름과 점수 리스트를 받아 성적표를 출력하는 함수를 만드세요.
요구사항:
- 평균, 최고점, 최저점 출력
- 평균에 따른 등급 출력 (90↑: A, 80↑: B, 70↑: C, 60↑: D, 나머지: F)
'''
def print_report(name, scores):
    print(f"=== {name} 성적표 ===")
    print(f"점수: {scores}")

    avg = sum(scores) / len(scores)
    print(f"평균: {avg}점")
    print(f"최고점: {max(scores)}점")
    print(f"최저점: {min(scores)}점")

    grade = (lambda x:
             "A" if x >= 90 else
             "B" if x >= 80 else
             "C" if x >= 70 else
             "D" if x >= 60 else
             "F")
    print(f"등급: {grade(avg)}")
print_report("김철수", [85, 92, 78, 96, 88])

'''
3. 비밀번호가 조건을 만족하는지 검증하는 함수를 만드세요.
조건:
- 8자 이상
- 숫자 포함
- 대문자 포함
'''
def validate_password(password):
    import numbers
    # 여기에 코드 작성
    if len(password) < 8:
        return (False, "8자 이상이어야 합니다")
    if not any(i.isdigit() for i in password):
        return (False, "숫자를 포함해야 합니다")
    if not any(i.isupper() for i in password):
        return (False, "대문자를 포함해야 합니다")
    return (True, "유효한 비밀번호입니다.")
print(validate_password("abc"))        # (False, "8자 이상이어야 합니다")
print(validate_password("abcdefgh"))   # (False, "숫자를 포함해야 합니다")
print(validate_password("abcdefg1"))   # (False, "대문자를 포함해야 합니다")
print(validate_password("Abcdefg1"))   # (True, "유효한 비밀번호입니다")


