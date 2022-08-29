import sys

def backTracking(idx):
    if len(case) == 6:
        for i in range(6):
            print(case[i],end=' ')
        print()
        return

    for i in range(idx,array[0]+1):
        if len(case) > 0:
            if case[-1] >= array[i]:
                continue
        case.append(array[i])
        backTracking(idx+1)
        case.pop()
    return

while True:
    array = list(map(int,sys.stdin.readline().rstrip().split(' ')))
    if not array[0]:
        break
    case = []
    backTracking(1)
    print()

