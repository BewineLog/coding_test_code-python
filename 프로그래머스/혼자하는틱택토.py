def get_count(board):
    o = 0
    x = 0

    for i in board:
        o += i.count('O')
        x += i.count('X')

    return (o, x)


def get_game_set(board, o, x):
    horizontal = []
    vertical = [''] * 3
    diagonal = [''] * 2

    for i in range(len(board)):
        diagonal[0] += board[i][i]
        diagonal[1] += board[2 - i][i]

    for i in range(len(board)):
        for j in range(len(board)):
            vertical[j] += board[i][j]

    for line in board:
        if line[0] == line[1] and line[1] == line[2]:
            horizontal.append(line[0] * 3)

    fin = horizontal + vertical + diagonal

    if 'OOO' in fin and 'XXX' in fin:
        return 0
    elif ('XXX' in fin and o != x):  # "XXX"만 완성되면 O와 X의 갯수는 동일해야한다
        return 0
    elif ('OOO' in fin and x >= o):  # "OOO"만 완성되면 O의 갯수는 무조건 X의 갯수보다 많아야한다.
        return 0

    return 1


def solution(board):
    o, x = get_count(board)
    if o < x or o > x + 1:
        return 0

    return get_game_set(board, o, x)
