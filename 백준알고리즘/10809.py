import sys

s = str(sys.stdin.readline())
val = ord('a')
alpha = [chr(val+i) for i in range(26)]

for i in alpha:
    try:
            print(s.index(i),end=' ')
    except:
        print('-1',end=' ')
print()
