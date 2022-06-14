"""
-기출 핵심 유형

- 학생들에게 0 ~ N 까지의 번호 부여.
- 처음에는 모든 학생들이 서로 다른 팀으로 구분 되어, 총 N+1개 팀 존재.
- 선생님이 할 수 있는 연산: 팀 합치기, 같은 팀 여부 확인
"""
import sys

def find_parent(parent,x):
    if parent[x] != x:  # 자기 자신이 부모가 아닐 경우
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int,input().split())  # 학생 수, 연산의 개수
parent = [0] * (n+1)

for i in range(0,n+1):  # 부모 정보 저장하는 배열 초기화
    parent[i] = i

# 연산 수행
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())

    if a == 0:  # 팀 합치기 연산
        union_parent(parent,b,c)
    else:   # 같은 팀 여부 확인 연산
        if find_parent(parent,b) == find_parent(parent,c):
            print('YES')
        else:
            print('NO')
