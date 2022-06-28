d = int(input())
l = list(map(int,input().split()))
cnt = 0

for i in range(0,len(l)):
    if l[i] == d:
        cnt += 1
print(cnt)
