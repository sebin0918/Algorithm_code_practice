import sys
input = sys.stdin.readline
n = int(input())
card = list(map(int, input().split()))
m = int(input())
mine = list(map(int, input().split()))

card.sort()
dic = {}

for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
for i in mine:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print('0', end= ' ')