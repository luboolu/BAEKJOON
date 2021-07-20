#BAEKJOON 2292번

n = int(input())

## 1 7 19 37 61 91
##  6 12 18 24 30
an = 0
i = 1
while True:
    an = 1 + 6 * ((i * (i - 1))/2)

    if n <= an:
        print(i)
        break

    i += 1