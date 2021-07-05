"""
-프로그래머스 코딩테스트 문제:"K번째 수"
-정렬
"""
def solution(array, commands):
    #return [sorted(array[i-1:j])[k-1] for i,j,k in commands]
    answer = []

    for command in commands:
        i,j,k = command
        
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer
