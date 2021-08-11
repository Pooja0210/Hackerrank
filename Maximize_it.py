from itertools import product
k,m = map(int,input().split())
def Square(n):
    return int(n)**2
l1 = []
for i in range(k):
    l1.append(list(map(Square,input().split()[1:])))
Max=0
for T in product(*l1):
    Sum =sum(T)%m
    if Sum > Max:
        Max = Sum
print(Max)
