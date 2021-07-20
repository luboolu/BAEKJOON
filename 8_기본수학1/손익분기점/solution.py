#BAEKJOON 1712번
import math

num = list(map(int, input().split(" ")))

#num0 : 고정비용, num1 : 가변비용, num2 : 노트북 가격
cost = num[0]
sales = 0
notebook = 0

if num[2] - num[1] <= 0:
    print(-1)
else:
    print(math.ceil(num[0] // (num[2] - num[1]) + 1))

# while True:
#     notebook += 1
#     sales += num[2]
#     cost += num[1]
#
#     if cost < sales:
#         print(notebook)
#         break



