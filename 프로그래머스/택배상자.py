from collections import deque


def solution(order):
    answer = 0
    q = deque()
    now = 0

    for i in range(len(order)):
        if i + 1 != order[now]:
            q.append(i + 1)

        if i + 1 == order[now]:
            answer += 1
            now += 1

        while q and q[-1] == order[now]:
            q.pop()
            answer += 1
            now += 1

    return answer
