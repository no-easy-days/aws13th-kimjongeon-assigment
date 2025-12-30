# 1. 사용자로부터 이메일 주소를 입력받아 사용자 이름과 도메인을 분리하여 출력하세요.
while True:
    email = input("이메일을 입력하세요: ")
    if "@" not in email:
        print("이메일 형식이 아닙니다. ")
        continue

    user, domain = email.split("@")
    print("사용자 이름: ", user)
    print("도메인: ", domain)
    break

# 2. 비밀번호가 8자 이상인지 확인하는 프로그램을 작성하세요.
# 조건: 길이가 8자 이상이면 "✅ 유효한 비밀번호입니다." 출력
password = input("비밀번호 유효성 검사: ")
if len(password) >= 8:
    print("✅ 유효한 비밀번호입니다.")
else:
    print("비밀번호는 8자 이상 입력해야합니다.")

# 3. 1부터 20까지의 숫자 중에서 3의 배수만 리스트에 담아 출력하세요.
res = []
for i in range(3, 21, 3):
    res.append(i)
print(res)

# 4. 철수와 영희의 관심사 리스트가 주어졌을 때, 공통 관심사를 찾아보세요.
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]
res = []
for c in chulsoo:
    for y in younghee:
        if c == y:
            res.append(c)
            break
print(res)

# ## 모범 답안
# set_chulsoo = set(chulsoo)
# set_younghee = set(younghee)
#
# # 교집합 구하기 (둘 다 좋아하는 것)
# common = set_chulsoo & set_younghee
# print(common)

# 5. 학생들의 점수가 딕셔너리로 주어졌을 때, 최고 점수를 받은 학생을 찾아보세요.
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}
max_score = 0
max_name = ""
for name, score in scores.items():
    if max_score < score:
        max_score = score
        max_name = name
print(f"{max_name}의 점수: {max_score}")
