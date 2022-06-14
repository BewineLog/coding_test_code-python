"""
-두 배열의 원소 교체
-국제 알고리즘 대회

-두 배열 모두 N개의 원소로 구성 & 원소는 모두 자연수
-K번의 바꿔치기 연산 가능, 각 배열의 원소를 골라서 바꾸는 것을 말함.
-> 최종 목표: 배열 A의 모든 원소의 합이 최대가 되도록 하는 것
"""

n,k = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i],B[i]= B[i],A[i]
    else:
        break

"""
result = 0
for i in A:
    result += i
print(result)
"""
print(sum(A))
