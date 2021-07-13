#BAEKJOON 8958번

n = int(input())

for i in range(n):
    a = list(input())
    s = []
    cont = 0
    for j in range(len(a)):
        if a[j] == "O":
            cont += 1
            s.append(cont)
        else:
            cont = 0
            s.append(0)

    print(sum(s))

