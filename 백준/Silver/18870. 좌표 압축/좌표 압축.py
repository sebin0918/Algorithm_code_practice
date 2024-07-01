n = int(input())
arr = list(map(int, input().split()))

arr1 = sorted(list(set(arr)))
dic = {arr1[i] : i for i in range(len(arr1))}

for i in arr:
    print(dic[i], end= ' ')

