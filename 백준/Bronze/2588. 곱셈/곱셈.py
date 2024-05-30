a = int(input())
b = input()

for i in range(3, 0, -1):
    print(a*int(b[i-1]))
    
print(a*int(b))



a = int(input())
b = input()

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))
