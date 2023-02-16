import heapq
def solution(book_time):
    answer = 0
    heap = []
    bt = [(int(s[:2])*60+int(s[3:]),int(e[:2])*60+int(e[3:]))for s,e in book_time]
    bt.sort()
    
    for s,e in bt:
        if not heap:
            heapq.heappush(heap,e+10)
            continue
        
        if heap[0] <=s:
            heapq.heappop(heap)
        else:
            answer += 1
            
        heapq.heappush(heap,e+10)
    
    return answer+1
