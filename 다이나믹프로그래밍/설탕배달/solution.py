#BAEKJOON 2839번

n = int(input())
result = 0

##n = 3a + 5b 인 경우를 찾아야함

while n >= 0:
    result += 1
    if n - 5 >= 0:
        n -= 5
    elif n - 3 >= 0:
        n -= 3
    else:
        result = -1
        break

print(result)