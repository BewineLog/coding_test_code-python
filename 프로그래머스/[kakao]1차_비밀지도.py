from collections import deque
def solution(n, arr1, arr2):
    answer = [''] * n
    for i in range(n):
        tval = bin(arr1[i]|arr2[i])[2:]
        tval = tval.rjust(n,'0')
        tval = tval.replace('1','#')
        tval = tval.replace('0',' ')
        answer[i] = tval
        
        
    return answer
