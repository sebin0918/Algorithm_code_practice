N = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    err = 0
    if i>1:
        for j in range(2, i):
            if i%j == 0:
                err += 1
        if err == 0:
            cnt += 1
print(cnt)
        
