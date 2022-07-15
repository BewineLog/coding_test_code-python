import sys
sen = list()
n = int(input())

for i in range(n):
    sen.append(str(sys.stdin.readline()[:-1]))
sen = list(set(sen))
sen.sort()
sen.sort(key = len )


for i in sen:
    print(i)
