num = int(input())
lst = list()

for i in range(0,num):
    lst.append(float(input()))
    
for i in range(0,num):
    print("${:.2f}".format(lst[i]*0.8))
