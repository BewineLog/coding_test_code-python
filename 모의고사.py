"""
-프로그래머스 코딩테스트 문제: "모의고사"
"""
def solution(answers):
    answer = []
    pat_one = [1,2,3,4,5]
    pat_two = [2,1,2,3,2,4,2,5]
    pat_three = [3,3,1,1,2,2,4,4,5,5]
    
    count = [0] * 3
    
    for idx,val in enumerate(answers):
        if val == pat_one[idx%len(pat_one)]:
            count[0] += 1
        if val == pat_two[idx%len(pat_two)]:
            count[1] += 1
        if val == pat_three[idx%len(pat_three)]:
            count[2] += 1
    
    
    max_cnt = max(count)
    for i in range(len(count)):
        if count[i] == max_cnt:
            answer.append(i+1)
    return answer
