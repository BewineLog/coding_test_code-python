import math

def isPrime(k):
    if k in (2, 3):
        return True
    if k in (0, 1) or k % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(k)) + 1, 2):
        if k % i == 0:
            return False
    return True


def dfs(prev, num, numbers, visited):
    for i in range(len(numbers)):
        if visited[i]:
            continue
        visited[i] = True
        if prev + numbers[i] not in num and isPrime(int(prev + numbers[i])):
            num.append(prev + numbers[i])
        dfs(prev + numbers[i], num, numbers, visited)
        visited[i] = False


def solution(numbers):
    numbers = list(numbers)
    visited = [False] * len(numbers)
    prev = ''
    num = []

    dfs(prev, num, numbers, visited)

    return len(set(list(map(int, num))))
