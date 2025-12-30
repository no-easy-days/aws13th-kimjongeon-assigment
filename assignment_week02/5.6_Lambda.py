# 1. 다음 도시 목록을 인구수 기준으로 정렬하세요.
cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]
sort_cities = sorted(cities, key=lambda x: x["population"])
for i in sort_cities:
    print(f"{i["name"]}: {i["population"]:,}명")

# 2. 문자열 리스트를 정수 리스트로 변환하고, 각 숫자에 100을 더하세요.
str_numbers = ["10", "20", "30", "40", "50"]

#lambda
int_numbers_lambda = list(map(lambda x: int(x)+100, str_numbers))
print(int_numbers_lambda)
#comprehension
int_numbers_comp = [int(i)+100 for i in str_numbers]
print(int_numbers_comp)

# 3. 할인율이 20% 이상인 상품만 추출하세요.
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]
#lambda
discounted_lambda = list(filter(lambda i: i["discount"] >= 20, products))
print(discounted_lambda)
#comprehension
discounted_comp = [i for i in products if i["discount"] >= 20]
print(discounted_comp)


