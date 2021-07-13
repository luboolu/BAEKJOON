#BAEKJOON 10870번

def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)

n = int(input())
print(fibonachi(n))