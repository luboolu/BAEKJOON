#BAEKJOON 10809번

s = input()
## a = 97, z = 122
answer = [-1 for i in range(26)]

for i in range(len(s)):
    #s[i]
    ascii_num = ord(s[i])

    if answer[ascii_num - 97] == -1:
        answer[ascii_num - 97] = i

answer = list(map(str, answer))
print(" ".join(answer))