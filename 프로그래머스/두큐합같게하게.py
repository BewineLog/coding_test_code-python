from collections import deque


def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    s = (sum1 + sum2) / 2

    if s - int(s) > 0 or max(queue1) > int(s) or max(queue2) > int(s):
        return -1

    dq1 = deque(queue1)
    dq2 = deque(queue2)

    while dq1 and dq2 and sum1 != sum2 and answer <= 600000:
        if sum1 < sum2:
            v = dq2.popleft()
            dq1.append(v)

            sum1 += v
            sum2 -= v
        else:
            v = dq1.popleft()
            dq2.append(v)

            sum1 -= v
            sum2 += v
        answer += 1

    return answer if sum1 == sum2 else -1
