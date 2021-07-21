#BAEKJOON 2798번

n, m = map(int,input().split())
card = list(map(int, input().split()))
sum = []

for i in range(len(card)):
    for j in range(len(card)):
        for k in range(len(card)):
            if i != j and i != k and j != k:
                sum.append(card[i] + card[j] + card[k])

sum = list(set(sorted(sum)))
dif = []
for i in range(len(sum)):
    if sum[i] > m:
        dif.append(999999)
    else:
        dif.append(abs(m - sum[i]))

print(sum[dif.index(min(dif))])