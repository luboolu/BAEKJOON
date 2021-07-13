#BAEKJOON 2577번

a = int(input())
b = int(input())
c = int(input())

abc = list(str(a * b * c))
abc = sorted(abc)

otn = [0,0,0,0,0,0,0,0,0,0]

for n in abc:
    otn[int(n)] += 1

for o in otn:
    print(o)