N, M = map(int, input().split())
basket = [0]*N

for _ in range(M):
    i, j, k = map(int, input().split())
    for a in range(i, j+1):
        basket[a-1] = k
for i in range(N):
    print(basket[i], end = ' ')

