cnt = int(input())
array  = [[0]*100 for i in range(100)]

for i in range(cnt):
    x, y = list(map(int, input().split()))
    
    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1
result = 0
for i in array:
    result += i.count(1)
    
print(result)