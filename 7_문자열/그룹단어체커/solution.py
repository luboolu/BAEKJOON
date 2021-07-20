#BAEKJOON 1316범

N = int(input())
answer = 0

for n in range(N):
    word = list(input())
    word_set = list(set(word))
    group = []

    isGroup = True
    for w in word:
        if w not in group:
            group.append(w)

        else:
            if group[-1] != w:
                isGroup = False

    if isGroup == True:
        answer += 1


print(answer)

