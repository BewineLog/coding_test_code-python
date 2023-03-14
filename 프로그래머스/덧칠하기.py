from collections import deque
def solution(n, m, section):
    answer = 0
    s = deque(section)
    while s:
        val = s[0]
        while s and val <= s[0] <= val + m-1:
            s.popleft()
        answer += 1
    return answer
