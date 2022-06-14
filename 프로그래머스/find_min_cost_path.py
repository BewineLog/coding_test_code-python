"""
-M 기업 코딩테스트

-N개의 회사 존재, 각회사는 서로 도로를 통해 연결되어 있다.
-방문 판매원 A는 현재 1번 회사에 위치해 있으며, X번 회사에 방문해 물건을 판매하고자 한다.

-도로는 양뱡향으로 이동 가능하며, 특정 회사와 다른 회사가 도로로 연결 되어 있다면 cost = 1로 이동 가능하다.
-소개팅 하고자 하는 사람은 K번 회사에 존재하고 있다.

-A는 1번 회사에서 K번 회사에 들렸다가, X번 회사로 가는 것이 목표.
-최소 시간을 계산하는 프로그램을 작성하시오.
->경유지를 거쳐 가는 문제이므로 플로이드-워셜 문제
"""
import sys

INF = int(1e9)

n,m = map(int,input().split())  # 회사 갯수, 도로 갯수

graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

m,k = map(int,input().split())  # 목표 회사, 경유 회사

distance = graph[1][k] + graph[k][m]

if distance >= INF:
    print('-1')
else:
    print(distance)

