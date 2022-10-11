num = 65536
def solution(str1, str2):
    answer = 0
    alphabet = [chr(c) for c in range(ord('a'),ord('z')+1)]
    dic1 = dict()
    dic2 = dict()
    
    ls1 = len(str1)
    ls2 = len(str2)
    
    token1 = []
    token2 = []
    
    for i in range(ls1-1):
        key = str1.lower()[i:i+2]
        if key.isalpha():
            if dic1.get(key):
                dic1[key] += 1
            else:
                dic1[key] = 1

    for i in range(ls2-1):
        key = str2.lower()[i:i+2]
        if key.isalpha():
            if dic2.get(key):
                dic2[key] += 1
            else:
                dic2[key] = 1
    
    # intersection
    int_val = 0
    for i in dic1.keys():
        if i in dic2.keys():
            int_val += min(dic1[i],dic2[i])
    #Union 구하기
    uni_val = 0
    for i in dic1.keys():
        if i in dic2.keys():
            uni_val += max(dic1[i],dic2[i])
            dic2.pop(i)
        else:
            uni_val += dic1[i]
            
    for i in dic2.keys():
        uni_val += dic2[i]
        
    
    if uni_val == 0:
        answer = num
    else:
        answer=int(int_val/uni_val * num)
    
    return answer
