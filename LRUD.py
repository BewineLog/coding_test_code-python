"""
-상하좌우 문제
-상하 / 좌우 index: 1 ~ N
-여행객이 상,하,좌,우 방향으로 이동. (by 계획서 기준, LRUD로 방향 표시함)
"""
n = int(input('size>'))
plan = list(map(str,input().split()))

row = 1 #UD
column = 1 #LR
i = 0

for way in plan:
    if way == 'R' and column + 1 <= n:
        column += 1
    elif way == 'L' and column -1 >= 1:
        column -= 1
    elif way == 'U' and row - 1 >= 1:
        row -= 1
    elif way == 'D' and row +1 <= n:
        row += 1

print('(',end='')
print(row,column,end='')
print(')')

"""이중 for문으로 구현하는 방법(n,plan) 그대로 사용"""
x,y = 1,1

#L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types=['L','R','U','D']

for p in plan:
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x,y = nx,ny

print(x,y)




