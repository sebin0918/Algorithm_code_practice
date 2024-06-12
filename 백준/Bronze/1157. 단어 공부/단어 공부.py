word = input().upper()
word_list = list(set(word))
cont=[]

for i in word_list:
    count = word.count(i)
    cont.append(count)

if cont.count(max(cont))>=2:
    print("?")
else:
    print(word_list[cont.index(max(cont))])