"""
-greedy algorithm, 모험가 길드 문제

-한 마을에 N명의 모험가
-모험가의 '공포도' 측정, 공포도가 높으면 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다.

-모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 그룹에 참여해야 여행을 떠날 수 있다.

-> 최대 몇개의 모험가 그룹을 만들 수 있는지 구하는 프로그램을 작성하시오.
"""
n = int(input())
data = list(map(int,input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)
