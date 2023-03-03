from collections import Counter
def solution(k, tangerine):
    answer = 0
    dic = Counter(tangerine)
    # print(dic)
    # for i in tangerine:
    #     dic[str(i)] = 1 if str(i) not in dic.keys() else dic[str(i)] + 1
    
    for i in dic.most_common():
        answer += 1
        k -= i[1]
        if  k <=0:
            break
        
    return answer
