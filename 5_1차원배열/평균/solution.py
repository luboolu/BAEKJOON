#BAEKJOON 1546번

n = int(input())
score = list(map(int, input().split()))
m = max(score)
new_mean = 0

for s in score:
    new_mean += s / m * 100

print(new_mean / len(score))

