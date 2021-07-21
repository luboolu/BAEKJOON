#BAEKJOON 2447번

def star(n):
    if n < 3:
        return 0
    else:
        print("***")
        print("* *")
        print("***")

n = int(input())
print(star(n))