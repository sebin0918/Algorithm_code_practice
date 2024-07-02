import sys
input = sys.stdin.readline

n = int(input())
N = list(map(int, input().split()))

m = int(input())
M = list(map(int, input().split()))

dic = {}
for i in range(n):
    dic[N[i]] = -1
    
for i in M:
    if i in dic:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
