from collections import deque


def search(r, c, maps, distance):
    visited = []
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque([(r, c)])

    while q:
        x, y = q.popleft()

        if (x, y) in visited:
            continue
        visited.append((x, y))
        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or maps[nx][ny] == 'X' or (nx, ny) in visited:
                continue
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))


def solution(maps):
    answer = 0
    maps = [list(line) for line in maps]
    distance = [[0] * len(maps[0]) for _ in range(len(maps))]
    sr, sc, lr, lc, er, ec = 0, 0, 0, 0, 0, 0

    for i in range(len(maps)):
        if 'S' in maps[i]:
            sr, sc = i, maps[i].index('S')
        if 'L' in maps[i]:
            lr, lc = i, maps[i].index('L')
        if 'E' in maps[i]:
            er, ec = i, maps[i].index('E')

    search(sr, sc, maps, distance)
    if distance[lr][lc] == 0:
        return -1

    answer += distance[lr][lc]
    distance = [[0] * len(maps[0]) for _ in range(len(maps))]
    search(lr, lc, maps, distance)
    if distance[er][ec] == 0:
        return -1
    return answer + distance[er][ec] 
