check = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()

for i in check:
    a = a.replace(i, '*')
print(len(a))