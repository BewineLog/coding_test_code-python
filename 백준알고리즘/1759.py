import sys

l, c = map(int,sys.stdin.readline().rstrip().split(' '))

if not (3 <= l <= c <= 15):
    sys.exit(0)

vowel = ['a','e','i','o','u']

stringList = sorted(list(sys.stdin.readline().rstrip().split(' ')))
case = []
vowel_cnt = 0

def backTracking(idx):
    global vowel_cnt
    if len(case) == l:
        if vowel_cnt < 1 or len(case)-vowel_cnt < 2:    # 모음 갯수가 1보다 작거나 자음 갯수가 2보다 작으면 출력하지 않고 return
            return
        for i in range(l):  # 문자열 출력
            print(case[i], end='')
        print()
        return

    for i in range(idx,c):
        if len(case) > 0 and case[-1] >= stringList[i]:  # 영문이 역순으로 들어가지 않도록 처리
            continue
        if stringList[i] in vowel:  # 모음 갯수 count
            vowel_cnt += 1

        case.append(stringList[i])
        backTracking(idx+1)
        pop_char = case.pop()

        if pop_char in vowel:   # 모음이 빠질 경우 모음 갯수에서 1 빼줌
            vowel_cnt -= 1

backTracking(0)
