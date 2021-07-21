#BAEKJOON 2231번

n = input()
sub_sum = 0

for i in range(1, int(n) + 1):
    str_i = str(i)
    sub_sum = i
    sum = i
    for j in str_i:
        sum += int(j)

    if sum == int(n):
        print(sub_sum)
        break
    if i == int(n):
        print(0)
        break

