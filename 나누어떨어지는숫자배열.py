"""
-프로그래머스 코딩테스트 문제: "나누어 떨어지는 숫자 배열"
"""
def solution(arr, divisor):
    #answer =[]

    return sorted([i for i in arr if i % divisor == 0 ]) or [-1]
