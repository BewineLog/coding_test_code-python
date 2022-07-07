import sys

t = int(sys.stdin.readline())

for _ in range(t):
    h,w,n = map(int,sys.stdin.readline().split())


    floor = n % h if n % h != 0 else h
    pos = (n-1) // h + 1
    pos = '0'+str(pos) if len(str(pos)) == 1 else str(pos)
    print(floor,pos,sep='')
