import string
S=input()
aList = list(string.ascii_lowercase)

for i in aList:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')

