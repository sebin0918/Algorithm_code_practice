angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())

if (angle_1 == angle_2) & (angle_1 == angle_3) & (angle_1 == 60):
    print("Equilateral")
elif (angle_1 + angle_2 + angle_3) == 180:
    if (angle_1 == angle_2) or (angle_2 == angle_3) or (angle_1 == angle_3):
        print("Isosceles")
    elif (angle_1 != angle_2) & (angle_1 != angle_3) & (angle_2 != angle_3):
        print("Scalene")
elif (angle_1 + angle_2 + angle_3) != 180:
    print("Error")