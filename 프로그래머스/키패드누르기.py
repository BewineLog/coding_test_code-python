"""
-프로그래머스 코딩테스트 문제: "키패드 누르기"
-카카오 인턴십 기출
"""
import math

def solution(numbers, hand):
    answer = ''
    pos = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    l_pos = '*'
    r_pos = '#'

    for x in numbers:
        if x in [1,4,7]:
            answer += 'L'
            l_pos = x
        if x in [3,6,9]:
            answer += 'R'
            r_pos = x
        if x in [2,5,8,0]:
            if l_pos == '*':
                l_x, l_y = (3, 0)
            else:
                l_x, l_y = pos[l_pos]

            if r_pos == '#':
                r_x, r_y = (3, 2)
            else:
                r_x, r_y = pos[r_pos]

            t_x, t_y = pos[x]

            #거리를 칸 수로 계산
            distance_l = abs(l_x-t_x) + abs(l_y-t_y)
            distance_r = abs(r_x-t_x) + abs(r_y - t_y)

            if distance_l > distance_r:
                r_pos = x
                answer += 'R'
            elif distance_l < distance_r:
                l_pos = x
                answer += 'L'
            else:  # distance가 동일할 때
                if hand == "left":
                    l_pos = x
                    answer += 'L'
                if hand == "right":
                    r_pos = x
                    answer += 'R'

    return answer
