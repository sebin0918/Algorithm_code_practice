import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
s = set()
count = 0

for i in range(n):
    s.add(input().rstrip())
for i in range(m):
    if input().rstrip() in s:
        count += 1
        
print(count)
    