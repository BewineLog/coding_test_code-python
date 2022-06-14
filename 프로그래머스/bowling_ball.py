"""
-2019 SW 마에스트로 입학 테스트

-볼링공 고르기 문제
-A,B 두 사람이 볼링을 치고 있다.
-두 사람은 무게가 서로 다른 볼링공을 고르려고 한다.
-볼링공은 총 N개가 있으며, 각 볼링공 마다 무게가 적혀있고, 공의 번호는 1번부터 순서대로 부여된다.
-볼링공의 무게는 1 ~ M 까지 존재하며, 같은 무게의 공이 존재할 수 있지만, 서로 다른 공으로 간주한다.

-> N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하시오.
"""
import sys

n, m = map(int, input().split())

input_weight = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(0,n-1):
    for j in range(i+1,n):
        if input_weight[i] != input_weight[j]:
            result += 1
print(result)

