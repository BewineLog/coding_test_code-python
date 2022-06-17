import sys

atoz = "abcdefghijklmnopqrstuvwxyz"

l = int(input())
estr = str(input())
ans = 0

for idx,char in enumerate(estr):
    ans += (atoz.find(char)+1) * (31**idx)

print(ans % 1234567891)
