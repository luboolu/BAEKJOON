#BAEKJOON 7568번

N = int(input())
data = []
for n in range(N):
    tmp = list(map(int, input().split()))
    data.append(tmp)

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j:
            if data[j][0] > data[i][0] and data[j][1] > data[i][1]:
                rank += 1

    print(rank,end=" ")