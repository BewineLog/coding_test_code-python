from collections import deque


def solution(storey):
    answer = 0
    q = deque([i for i in str(storey)[::-1]])
    roundup = 0

    while q:
        num = int(q.popleft())

        if roundup == 1:
            num += 1
            roundup = 0

        answer += num if 10 - num > num else 10 - num
        roundup = 1 if 10 - num < num else 1 if q and num == 5 and int(q[0]) >= 5 else 0

    return answer + 1 if roundup == 1 else answer
