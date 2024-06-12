alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
time = 0

# 입력받은 문자열의 각 문자에 대해 반복
for i in range(len(S)):
    # 다이얼 그룹 각각에 대해 반복
    for j in alpha:
        # 현재 문자가 다이얼 그룹에 있는지 확인
        if S[i] in j:
            # 인덱스의 값에 +3을 해서 시간 측정
            time += alpha.index(j)+3
print(time)