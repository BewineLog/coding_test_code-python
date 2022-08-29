n = int(input())
board = [0] * n
visited = [0]*n
count = 0


def checkAvailable(col):
    for i in range(col):
        if abs(board[col] - board[i]) == col - i:
            return False
    return True

def searchGraph(col):
    global count
    if col == n:
        count += 1
        return

    for i in range(n):
        if col == 0 and n % 2 == 0 and i == n/2:  # 보드가 짝수 size 일 경우, 대칭이기 때문에 *2 연산으로 연산 횟수 줄임
            return
        if visited[i]:
            continue
        board[col] = i
        if checkAvailable(col):
            visited[i] = True
            searchGraph(col+1)
            visited[i] = False

searchGraph(0)

if n % 2 == 0:
    print(count*2)
else:
    print(count)
