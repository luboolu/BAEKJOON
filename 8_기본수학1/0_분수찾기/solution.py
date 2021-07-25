#BAEKJOON 1193번
t = int(input())
n = 1
sum = 0

while True:
    sum += n
    if sum >= t:
        break
    else:
        n += 1

print(n)
print(sum)
m = n
if n % 2 == 0:
    #n 짝수
    pass

else:
    #n 홀수
    pass
