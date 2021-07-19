#BAEKJOON 5622번

nums = list(input())
numbers = []
time = 0
dials = [2, 3, 4, 5, 6, 7, 8, 9]
alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

for n in nums:
    for i in range(len(alp)):
        if n in alp[i]:
            time += i + 3

print(time)

