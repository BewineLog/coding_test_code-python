n, m = map(int,input().split())
data = list(map(int, input().split()))

array = [0] * 11 # m의 최대 값은 10

# 각 요소의 갯수 저장
for x in data:
    array[x] += 1

result = 0
# 각 무게에 대해서 연산
for i in range(1, m+1):
    n -= array[i] # 해당 요소까지의 갯수를 제외(구하는 것이 가능한 조합의 갯수이기 때문에)
    result += array[i] * n # (요소의 갯수) * (해당 요소까지의 갯수를 제외하고 남은 요소의 갯수)

print(result)
