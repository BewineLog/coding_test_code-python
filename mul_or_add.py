"""
-Facebook interview 문제

-곱하기 혹은 더하기 문제
-0~9까지의 숫자로만 문자열이 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하여
숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

* 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.
"""

s = str(input())

result = 0

for i in range(len(s)):
    if result == 0 or int(s[i]) == 0:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)