#BAEKJOON 10951번

answer = []
while True:
    try:
        inp = input()
        a, b = inp.split(" ")
        answer.append(int(a) + int(b))
    except:
        break

for i in range(len(answer)):
    print(answer[i])