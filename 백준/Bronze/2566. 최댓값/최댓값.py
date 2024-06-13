num_list = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_num_row = 0
max_num_column = 0
for i in range(9):
    for j in range(9):
        if max_num <= num_list[i][j]:
            max_num_row = i +1
            max_num_column = j +1
            max_num = num_list[i][j]
print(max_num)
print(max_num_row, max_num_column)