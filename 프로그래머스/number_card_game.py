"""
- 숫자 카드 게임 , 2019 국가 교육기관 코딩 테스트
- 각 행에서 가장 낮은 숫자 선정.
- 그 중 가장 높은 숫자 카드 한 장을 뽑는 게임
- N * M 형태(행,렬)
"""

n,m = map(int,input('행&렬 입력>').split())
array = []
min_val = []

for num in range(n):
    array.append(list(map(int,input().split())))
    min_val.append(min(array[num]))

print(array)
print(max(min_val))


