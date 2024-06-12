N = int(input())
group = 0
for j in range(N):
    word = input()
    err = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0:
                err += 1
    if err == 0:
        group += 1
print(group)