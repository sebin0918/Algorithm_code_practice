import math
a, b = map(int, input().split())
c, d = map(int, input().split())

e = a*d + b*c
f = b*d
gcd = math.gcd(e, f)
if gcd != 1:
    e//=gcd
    f//=gcd

print(e,f)