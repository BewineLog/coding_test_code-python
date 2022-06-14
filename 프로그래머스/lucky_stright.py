"""
-핵심 기출 문제

-캐릭터는 '럭키 스트레이트' 라는 기술 보유

<발동 조건>
- 현재 캐릭터의 점수를 N 이라고 할 때, 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분과 오른쪽 부분의 각 자릿수의 합이 동일 해야 사용할 수 있다.

->현재 점수 N이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 알려주는 프로그램을 작성하세요.
"""

n = str(input())
num = int(len(n))

left = 0
right = 0

for i in range(num//2):
    left += int(n[i])
    right += int(n[num//2+i])

if left == right:
    print('LUCKY')
else:
    print('READY')
