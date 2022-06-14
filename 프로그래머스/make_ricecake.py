"""
-떡 만들기
-높이 H를 지정할 경우, 높이가 H보다 낮은 떡은 잘리지 않는다.
-손님이 요청한 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 높이의 최댓값을 구하는 프로그램을 만들어라.
-> 높이의 범위: 1 ~ 20억(이진탐색으로 범위를 줄여 나가면 시간이 단축된다.)
"""

n,m = map(int,input().split())

x = list(map(int,input().split()))

#높이 이진탐색
start = 0
end = max(x)

while start <= end:
    mid = (start + end) // 2
    total = 0

    for i in x:
        if i - mid > 0:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid #최대한 덜 잘랐을 때가 정답이므로, 기록
        start = mid + 1

print(result)
