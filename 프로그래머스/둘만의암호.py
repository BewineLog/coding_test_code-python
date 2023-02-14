import string
def solution(s, skip, index):
    answer = ''

    alpha = [chr(i) for i in range(ord('a'),ord('z')+1) if chr(i) not in skip]
    
    
    return ''.join(alpha[(alpha.index(i) + index)% len(alpha)]for i in s)
