import sys
import math

n = int(input())
modular = 1000000007
total = 0
numerator = []
dominator = []


def getLcd(dominator:list):
    dom = dominator[0]
    for i in range(len(dominator)-1):
        dom = math.lcm(dom,dominator[i+1])
    return dom

def getFraction(numerator:list,dominator:list,dom):

    sumNumerator = 0

    for i in range(len(dominator)):
        sumNumerator += numerator[i] * (dom//dominator[i])
    return (sumNumerator,dom)


def DQ(num,x):
    if x == 1:
        return num
    tmp = DQ(num,x//2)
    if x % 2 == 1:
        return tmp *tmp* num % modular
    else:
        return tmp * tmp % modular


for _ in range(n):
    n, s = map(int,sys.stdin.readline().rstrip().split())
    numerator.append(s)
    dominator.append(n)

sumN, lcd = getFraction(numerator,dominator,getLcd(dominator))

total = DQ(lcd,modular-2)

print((sumN*total) % modular)
