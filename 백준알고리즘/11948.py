lst = [0] * 6

for i in range(0,6):
    lst[i] = int(input())

res = sum(lst) - min(lst[0],lst[1],lst[2],lst[3]) - min(lst[4],lst[5])
print(res)
