#BAEKJOON 1110번

n = input()
new_n = 0
cycle = 0

while n != new_n:
    cycle += 1

    a = n / 10 ##10의 자리 수
    b = n % 10 ##1의 자리 수


print(cycle)
