"""
-왕실의 나이트
-8x8 정원
-나이트는 L자 형태로만 이동 가능(수평 2 & 수직 1 or 수평 1 & 수직 2)
-정원 밖으로는 나갈 수 없다.
-위치가 주어졌을 때, 나이트가 이동할 수 있는 모든 경우의 수를 구해라
"""
pos = input('>') #ex) a1,c4,h3 etc...
row = int(pos[1])
col = int(ord(pos[0])) - int(ord('a')) + 1 #문자 정수형 변환

#나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

#8가지 방향에 대해서 이동할 수 있는지 확인
cnt = 0
for step in steps:
    #이동하고자 하는 위치
    next_row = row + step[0]
    next_col = col + step[1]

    #이동하고자 하는 위치로 이동 가능한지 확인
    if next_row >= 1 and next_row <=8 and next_col >= 1 and next_col <= 8:
        cnt += 1

print(cnt)


