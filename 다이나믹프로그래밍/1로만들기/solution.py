#BAEKJOON 1463번
x = int(input())
answer = 0

while True:
    if x == 1:
        break

    if x % 2 == 0 and (x // 2) % 2 == 0:
        x = x // 2
    elif x % 3 == 1:
        x -= 1
    elif x % 3 == 0:
        x = x // 3
    elif x % 2 == 0:
        x = x // 2
    else:
        x -= 1
    answer += 1
    print(x)
print(answer)