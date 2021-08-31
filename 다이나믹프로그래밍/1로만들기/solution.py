#BAEKJOON 1463번
x = int(input())
answer = 0

a1, a2 = divmod(x, 3)
b1, b2 = divmod(x, 2)

if a1 < b1:
    s = [3,2]
else:
    s = [2,3]

while True:
    if x % s[0] == 0:
        x = x // s[0]
    elif x % s[1] == 0:
        x = x // s[1]
    else:
        x -= 1
    answer += 1
    print(x)

    if x == 1:
        break

print(answer)




