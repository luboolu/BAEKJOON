#BAEKJOON 14681번

x = int(input())
y = int(input())

#1사분면 x > 0,y > 0
if x > 0 and y > 0:
    print(1)
#2사분면 x < 0, y > 0
elif x < 0 and y > 0:
    print(2)
#3사분면 x <  0, y < 0
elif x < 0 and y < 0:
    print(3)
#4사분면 x > 0, y < 0
else:
    print(4)