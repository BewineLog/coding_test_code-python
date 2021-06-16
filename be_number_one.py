"""
- 1이 될 때 까지, 2018 E 기업 알고리즘 대회
- 어떠한 수 N이 1이 될 때까지, 다음 두 과정 중 하나를 선택하여 반복적 수행(최소 횟수로)
1) N에서 1 빼기
2) N을 K로 나누기(단, N이 K로 나누어 떨어질 때만 가능)
"""

n,k = map(int,input().split())
m = n #두번째 방법용 변수

cnt = 0
while n >= k:
    while n % k != 0:
        n -= 1
        cnt += 1

    while n % k == 0:
        n /= k
        cnt += 1

while n != 1:
    n -= 1
    cnt += 1

print(cnt)

"""수학적인 접근"""
cnt = 0

while True:
    target = (m//k) * k
    m = m - target #뺄셈 횟수
    cnt += m

    m = target

    if m < k:
        break

    m //= k
    cnt += 1

cnt += m - 1 #m < k 일 때, 뺄셈 연산 횟수
print(cnt)


