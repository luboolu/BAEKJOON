##ver. for문
# n = int(input())
# answer = 1
#
# for i in range(n):
#     answer *= i + 1
#
# print(answer)



##ver. 재귀함수
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

n = int(input())
print(factorial(n))