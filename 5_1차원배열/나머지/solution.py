#BAEKJOON 3052번

n = []
d = []
for i in range(10):
    n.append(int(input()))
    d.append(int(n[i] % 42))

print(len(set(d)))