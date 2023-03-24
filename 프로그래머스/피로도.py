def dfs(k, answer, depth, dungeons, visited):
    answer = max(answer, depth)
    for i in range(len(dungeons)):
        if visited[i] or k < dungeons[i][0]: continue

        visited[i] = True
        answer = dfs(k - dungeons[i][1], answer, depth + 1, dungeons, visited)
        visited[i] = False
    return answer


def solution(k, dungeons):
    visited = [False] * len(dungeons)
    depth = 0
    answer = -1
    answer = dfs(k, answer, depth, dungeons, visited)

    return answer
