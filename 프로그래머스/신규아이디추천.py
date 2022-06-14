"""
-프로그래머스 코딩 테스트 문제: "신규 아이디 추천"
-카카오 블라인드테스트 기출 문제
"""
def solution(new_id):
    answer = ''
    
    #1단계
    new_id = new_id.lower()
    #2단계
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ["-","_","."]:
            answer += i

    #3단계
    while ".." in answer:
        answer = answer.replace("..",".")

    #4단계
    if len(answer) >= 2:
        if answer[-1] == ".":
            answer = answer[:-1]
        if answer[0] == ".":
            answer = answer[1:]
    else:
        if answer == ".":
            answer = ""
    #5단계
    if len(answer) == 0:
        answer += "a"
    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]
    #7단계
    if len(answer) <= 2:
        for i in range(3-len(answer)):
            answer += answer[-1]
            
    return answer
