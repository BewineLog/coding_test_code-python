from collections import deque
def solution(x, y, n):
    answer = 0
    dq = deque([x])
    distance = [0 for _ in range(1000001)]
    
    if x == y:
        return 0
    while dq:
        val = dq.popleft()
        
        if 1<= val*2 <= y and distance[val*2] ==0:
            distance[val*2] = distance[val]+1
            dq.append(val*2)
        if 1<= val*3 <= y and distance[val*3] ==0:
            distance[val*3] = distance[val]+1
            dq.append(val*3)
        if 1<= val+n <= y and distance[val+n] ==0:
            distance[val+n] = distance[val]+1
            dq.append(val+n)
        
    return distance[y] if distance[y] != 0 else -1
