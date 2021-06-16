"""
- 시각
- 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초 까지 모든 시각 중에서 3이 하나라도 포함되어 있는 경우의 수 구하기
"""
import time

# 1) 시간의 모든 경우의 수는 86,400 이므로 모든 경우의 수를 다 세어도 된다.
n = int(input('input hour:'))

second = 0
minute = 0
hour = 0

cnt  = 0
"""무한 loop로 계산하기"""
while True:
    second += 1

    if second == 60:
        second = 0
        minute += 1

    if minute == 60:
        minute = 0
        hour += 1

    if hour == n+1:
        break

    if second // 10 == 3 or second % 10 == 3 or minute // 10 == 3 or minute % 10 == 3 or hour // 10 == 3 or hour % 10 ==3:
        cnt += 1

print(cnt)

"""3중 for문으로 검색하기"""
cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
