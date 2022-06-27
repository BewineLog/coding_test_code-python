import sys

t = int(sys.stdin.readline())
lst = list()
for _ in range(t):
    age, name = map(str,sys.stdin.readline().split())
    age = int(age)

    lst.append((age,name))
lst.sort(key = lambda x : x[0])

for i in range(t):
    print(lst[i][0],lst[i][1])
