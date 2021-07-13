#BAEKJOON 4344번

c = int(input())
data = []
for i in range(c):
    data.append(list(map(int, input().split())))

for i in range(len(data)):
    score_sum = sum(data[i][1:])
    score_mean = score_sum / data[i][0]
    stu = 0
    for j in range(1, data[i][0] + 1):
        if data[i][j] > score_mean:
            stu += 1

    print(str('%.3f' % round((stu / data[i][0]) * 100, 3)) + "%")