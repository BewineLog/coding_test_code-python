N,M = map(int,input().split())

board = [[m for m in range(M)] for n in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = []

for i in range(N):
    board[i] = list(input())
#print(board)

def make_bw(start_col, end_col, start_row, end_row,board) -> int:
    cnt_b = 0
    cnt_w = 0

    temp_board = []

    for line in board[start_col:end_col]:
        temp_board.append(line[start_row:end_row])

    for i in range(8):
        for j in range(8):
            #(0,0) = W
            if (i % 2  == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                if temp_board[i][j] != 'W':
                    cnt_w += 1
            elif (i % 2  == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                if temp_board[i][j] != 'B':
                    cnt_w += 1
    for i in range(8):
        for j in range(8):
            #(0,0) = B
            if (i % 2  == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
                if temp_board[i][j] != 'B':
                    cnt_b += 1
            elif (i % 2  == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                if temp_board[i][j] != 'W':
                    cnt_b += 1
    return min(cnt_b,cnt_w)
                    
            


for i in range(8,N+1):
    for j in range(8,M+1):
        k = make_bw(i-8,i,j-8,j,board)
        count.append(k)

print(min(count))
