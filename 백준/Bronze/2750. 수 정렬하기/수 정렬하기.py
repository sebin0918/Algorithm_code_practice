N = int(input())
num_list = []

for i in range(N):
    num = int(input())
    num_list.append(num)
num_list1 = sorted(num_list)
for i in range(len(num_list)):
    print(num_list1[i])
    