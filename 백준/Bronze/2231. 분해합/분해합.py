N = int(input())
result = 0

for i in range(1, N+1):
    num = list(map(int, str(i)))
    result = sum(num) + i
    if result == N:
        print(i)
        break
    if i == N:
        print(0)