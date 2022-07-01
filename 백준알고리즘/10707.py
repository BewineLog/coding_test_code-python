A = int(input())
B = int(input())

C = int(input())
D = int(input())
P = int(input())

A_price = A * P
B_price = 0

if P <= C:
    B_price = B
else:
    B_price = B + D*(P-C)

print(min(A_price,B_price))
