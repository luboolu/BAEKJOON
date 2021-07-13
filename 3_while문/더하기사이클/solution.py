#BAEKJOON 1110번

n = int(input())
new_n = n
cycle = 0

while True:
    cycle += 1
    if new_n >= 10:
        a = int(new_n / 10) ##10의 자리 수
        b = int(new_n % 10) ##1의 자리 수
    else:
        a = 0
        b = int(new_n % 10)

    x = int((a + b) % 10)
    new_n = int(str(b) + str(x))

    if n == new_n:
        break

print(cycle)
