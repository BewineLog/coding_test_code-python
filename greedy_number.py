"""
실전문제 1) 큰 수의 법칙 // 2019 국가 교육기관 코딩테스트
Greedy Algorithm
-같은 인덱스의 요소를 한번에 더할 수 있는 최대 횟수 k, 총 더하는 횟수 m을 만족하는 총합의 최대 값을 구하는 문제
"""

n,m,k= map(int, input().split()) #n: 배열의 크기, m: 더하는 횟수, k: 같은 인덱스 요소를 연속해서 더할 수 있는 횟수
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

max= 0

"""수열을 통해서 최대 값 구하기"""
count = int(m/(k+1)*k) # 수열에서 제일 큰 요소가 등장하는 횟수
max += second * count / k # 수열 횟수만큼 두번째 큰 요소 더함.
count += m % (k+1) # 수열 이외 나머지 연산

max += first * count
print(int(max))


max = 0
"""Normal..?"""
while True:
    for _ in range(k):
        if m == 0:
            break
        max += first
        m -= 1

    if m == 0:
        break
    max += second
    m -= 1
print(int(max))
