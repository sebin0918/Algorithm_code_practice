num_list = []
for i in range(1, 6):
    num = int(input())
    num_list.append(num)
num_list.sort()
print(int(sum(num_list)/5))
print(num_list[2])