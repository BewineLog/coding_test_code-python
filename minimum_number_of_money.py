"""
-N가지 종류 화폐 중 최소한의 개수를 사용하여, 가치의 합을 M원 으로 만들기
"""
n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001]*(m + 1)

d[0] = 0

for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j],d[j-array[i]] + 1)

if d[m] == 10001:
    print('-1')
else:
    print(d[m])