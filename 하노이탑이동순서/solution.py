#BAEKJOON 11720

def hanoi(n, t1, t2, t3):
    if n == 1:
        print(t1, t3)
    else:
        hanoi(n - 1, t1, t3, t2)
        print(t1, t3)
        hanoi(n - 1, t2, t1, t3)

n = int(input())
num = 1

for i in range(n - 1):
    num = num * 2 + 1

print(num)
hanoi(n, 1, 2, 3)





# 1
# 2
# 3
#
# 2
# 3  1
#
#321
#
#  1
# 32
#
#  1
#  23
#
# 123
#
#   2
# 1 3
#
#   1
#   2
#   3