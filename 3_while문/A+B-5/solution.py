a = []
b = []

while True:
    x, y = input().split(" ")
    x = int(x)
    y = int(y)

    if x == 0 and y == 0:
        break
    else:
        a.append(x)
        b.append(y)

for i in range(len(a)):
    print(a[i] + b[i])
