#BAEKJOON 2839번

n = int(input())
result = 0

##n = 3a + 5b 인 경우를 찾아야함
if n % 5 == 0:
    result = n // 5
elif n % 3 == 0:
    result = n // 3
else:
    while True:
        if n % 3 != 0:
            n -= 5
            result += 1
        else:
            n -= 3
            result += 1

        if n == 0:
            break
        elif n < 0:
            result = -1
            break

print(result)