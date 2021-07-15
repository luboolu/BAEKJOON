#BAEKJOON 2908번

num1, num2 = map(int, input().split())
answer_1 = ""
answer_2 = ""
for i in range(len(str(num1))):
    answer_1 += str(num1)[-i - 1]

for i in range(len(str(num2))):
    answer_2 += str(num2)[-i - 1]

if answer_1 > answer_2:
    print(answer_1)
else:
    print(answer_2)