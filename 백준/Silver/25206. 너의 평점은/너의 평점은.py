# 학점과 점수를 매핑한 딕셔너리
lev = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 
       'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

# 총 학점과 총 점수를 저장할 변수를 초기화
total = 0.0
result = 0.0

# 20개의 과목에 대해 반복
for i in range(20):
    # 과목명, 학점, 등급을 입력받아 공백을 기준으로 분리
    subject, sub, grade = input().split()
    
    # 등급이 'P'가 아닌 경우만 계산에 포함
    if grade != 'P':
        # 학점을 실수형으로 변환하여 더함
        sub = float(sub)
        total += sub
        # 학점과 등급에 해당하는 점수를 곱하여 더함
        result += sub * lev[grade]

# 평균 학점을 계산하고 소수점 6자리까지 출력
print(format(result / total, ".6f"))
