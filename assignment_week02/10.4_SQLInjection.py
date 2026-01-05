"""
1. 아래 코드에서 위험한 부분을 찾고, 왜 위험한지 설명하세요.
name = input("이름: ")
age = input("나이: ")

sql = f"INSERT INTO students VALUES ('{name}', {age})"
cursor.execute(sql)

Sol)
input()으로 사용자가 SQL 문법 자체를 입력할 수 있어서 문제가 발생할 수 있다.
"""

"""
2. **안전한 코드로 수정하기**
위 코드를 Placeholder를 사용하여 안전하게 수정하세요.

Sol)
# f-string 대신 %s placeholder 사용

name = input("이름: ")
age = input("나이: ")

sql = "INSERT INTO students VALUES (%s, %s)"
cursor.execute(sql, (name, age))
"""

"""
3. 아래 취약한 코드가 있을 때, 어떤 입력값을 넣으면 모든 상품 정보를 볼 수 있을까

product_name = input("검색할 상품: ")
sql = f"SELECT * FROM products WHERE name = '{product_name}'"

Sol)
' OR 1=1 --
#1=1은 항상 참으로, 모든 상품이 조회된다
"""

"""
4. 아래 코드를 이름 기반 placeholder `%(key)s`를 사용하여 수정하세요.
같은 값을 여러 번 사용하는 경우의 장점을 확인해보세요.
"""
# 위험한 코드
keyword = input("검색어: ")
sql = f"""
    SELECT * FROM posts 
    WHERE title LIKE '%{keyword}%' 
    OR content LIKE '%{keyword}%'
    OR author LIKE '%{keyword}%'
"""
# 수정된 코드
keyword = input("검색어: ")
sql = """
    SELECT * FROM posts
    WHERE title LIKE %(kw)s
    OR content LIKE %(kw)s
    OR author LIKE %(kw)s
"""
cursor.execute(sql, {"kw": f"%{keyword}%"})




