"""
-프로그래머스 코딩테스트 문제: "무지의 먹방 라이브"
-카카오 블라인드 테스트 기출문제
"""
import heapq

def solution(food_times, k):
    answer = 0
    q = []
    
    if sum(food_times) <= k:
        return -1
    
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    sum_value = 0 #먹기 위해서 사용한 시간
    previous = 0 #직전에 다 먹은 음식 시간
    length = len(food_times) #남은 음식의 갯수
    
    while (sum_value + length*(q[0][0] - previous)) <=k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now
        
    result = sorted(q,key = lambda x: x[1])
    
    return result[(k - sum_value) % length][1]
