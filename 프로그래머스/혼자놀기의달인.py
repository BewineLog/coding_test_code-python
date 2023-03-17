# 두 개의 그룹의 곱이 최대가 되는 값을 찾아야한다.
# 그룹은 어떤 수로 시작해도 같은 그룹이 만들어진다.
def solution(cards):
    answer = 0
    group = []
    isopen = [-1] * len(cards)
    rnd = 1
    while isopen.count(-1) != 0:
        idx = isopen.index(-1)
        isopen[idx] = rnd
        while True:
            idx = cards[idx] - 1
            isopen[idx] = rnd
            if isopen[cards[idx] - 1] == rnd:
                break
        group.append(isopen.count(rnd))
        rnd += 1

    group.sort()
    return 0 if len(group) <= 1 else group[-1] * group[-2]
