import sys

n = int(sys.stdin.readline())


if n % 8 == 1:
    print('1')
elif n % 8 == 5:
    print('5')
elif n % 4 == 3:
    print('3')
elif n % 8 == 2 or n % 8 == 0:
    print('2')
else:
    print('4')
