#BAEKJOON 2675번

t = int(input())
r = []
s = []
for i in range(t):
    a, b = input().split()
    r.append(int(a))
    s.append(b)

for i in range(t):
    answer = ""
    for j in range(len(s[i])):
        for k in range(r[i]):
            answer += s[i][j]

    print(answer)


