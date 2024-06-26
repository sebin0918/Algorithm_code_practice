N, M = map(int, input().split())
board = []
result = []

for i in range(N):
    board.append(input())
    
for i in range(N-7):
    for j in range(M-7):
        w_index = 0
        b_index = 0
        for k in range(i, i+8):
            for g in range(j, j+8):
                if (k+g)%2 == 0:
                    if board[k][g] != 'W':
                        w_index += 1
                    else:
                        b_index += 1
                else:
                    if board[k][g] != 'W':
                        b_index += 1
                    else:
                        w_index += 1
        result.append(w_index)
        result.append(b_index)
print(min(result))