#BAEKJOON 4673번

def selfNum(n, m):
    num = int(n)
    str_num = str(n)

    for i in str_num:
        num += int(i)

    if num < 10000 and num in m:
        m.pop(m.index(num))
        return selfNum(num, m)
    else:
        return m

million = list(range(10000))

for i in range(10000):
    million = selfNum(i, million)

for m in million:
    print(m)


