import sys
from math import factorial as f
T = int(input())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(int(f(M)/(f(N)*f(M-N))))
