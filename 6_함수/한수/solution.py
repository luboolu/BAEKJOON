#BAEKJOOON 1065번

def hanSu(num):
    answer = 0

    for i in range(1, num + 1):
        str_num = str(i)

        isHanSu = True
        if i >= 100:
            ##한수인지 판단
            dif = int(str_num[0]) - int(str_num[1])
            for j in range(len(str_num)):
                if j > 0:
                    now_dif = int(str_num[j - 1]) - int(str_num[j])

                    if dif != now_dif:
                        isHanSu = False
                        break

        if isHanSu == True:
            answer += 1

    return answer


n = int(input())
print(hanSu(n))