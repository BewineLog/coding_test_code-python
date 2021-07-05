"""
-Facebook interview 문제

-문자열 재정렬
-알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
-이때, 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
"""

s = input()
value = 0
s_str=[]

for i in range(len(s)):
    if s[i].isalpha():
        s_str.append(s[i])
    if s[i].isdigit():
        value += int(s[i])

s_str.sort()

if value != 0:
    s_str.append(str(value))

print(''.join(s_str))

