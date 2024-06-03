X = int(input())
N = int(input())
pay = 0
for i in range(1, N+1):
    a, b = map(int, input().split())
    pay += (a*b)
    
if X == pay:
    print("Yes")
else:
    print("No")
