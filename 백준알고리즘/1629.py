import sys

a,b,c = map(int,sys.stdin.readline().split())

def DivideAndConquer(num1,num2):
    if num2 == 1:
        return num1 % c

    tmp = DivideAndConquer(num1,num2//2)
    if num2 % 2 == 0:
        return tmp ** 2 % c
    else:
        return tmp**2 * num1 % c
print(DivideAndConquer(a,b))
