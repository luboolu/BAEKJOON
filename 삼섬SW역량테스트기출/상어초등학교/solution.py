"""
BACKJOON 21608번 : 상어 초등학교

"""
##매개변수로 주어진 (now_r, now_c)에 인접한 자리를 반환
def near(n, now_r, now_c):
    ##인접한 자리 후보는 2개 또는 4개
    ##가능한 4가지의 경우를 모두 구하고, 존재하지 않는 자리는 지운다.
    nearSit = []
    answer = []

    nearSit.append((now_r - 1, now_c))
    nearSit.append((now_r, now_c - 1))
    nearSit.append((now_r + 1, now_c))
    nearSit.append((now_r, now_c + 1))

    for sit in nearSit:
        if sit[0] < 1 or sit[0] > n or sit[1] < 1 or sit[1] > n:
            pass
        else:
            answer.append(sit)

    return sorted(answer)

N = int(input()) ## N * N = 전체 학생수, 자리 수

##빈교실 만들기 - 자리 배치 결과를 저장할
classroom = []
for r in range(N):
    tmp = []
    for c in range(N):
        tmp.append(0)
    classroom.append(tmp)


std_order = [] ##자리배치를 하는 학생들의 순서
std_like = []  ##각 순서의 학생들이 좋아하는 학생 리스트(2차원)
for n in range(N * N):
    input_list = list(map(int, input().split()))

    my_std = input_list[0]   ##현재 학생
    my_like = input_list[1:] ##현재 학생이 좋아하는 학생

    std_order.append(my_std) ##자리배치 후 만족도를 구하기 위해 저장
    std_like.append(my_like) ##자리배치 후 만족도를 구하기 위해 저장

    info = []
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if classroom[r - 1][c - 1] == 0:
                like = 0
                empty = 0

                sit = near(N, r, c) ##인접한 자리를 찾아옴 [(r, c)] 형태로

                for s in sit:
                    if classroom[s[0] - 1][s[1] - 1] == 0:
                        empty += 1
                    elif classroom[s[0] - 1][s[1] - 1] in my_like:
                        like += 1

                info_rc = {"rc": (r, c), "like": like, "empty": empty}
                info.append(info_rc)

    ##이제 앉혀아지!!
    ##행, 열이 작은 순서대로 먼저 정렬
    ##1순위로 인접한 자리의 좋아하는 학생 수 2순위로 인접한 자리의 비어있는 자리의 수로 정렬

    i = 0
    info_sorted = sorted(info, key=(lambda x: (x["rc"])), reverse=False)
    info_sorted = sorted(info_sorted, key=(lambda x: (x["like"], x["empty"])), reverse = True)
    my_std_sit = info_sorted[i]["rc"]

    ##정렬 순서대로 학생을 자리에 앉힌다.
    ##우선순위에 있는 자리가 비어있지 않다면, 다음 순위의 자리로 넘어간다.
    while True:
        if classroom[my_std_sit[0] - 1][my_std_sit[1] - 1] == 0:
            classroom[my_std_sit[0] - 1][my_std_sit[1] - 1] = my_std
            break

        i += 1
        my_std_sit = info_sorted[i]["rc"]

##자리배치 후 만족도 계산 - 자리배치 순서대로
satisfaction = 0 ##전체 만족도
sat = [0, 1, 10, 100, 1000] ##좋아하는 학생의 인접한 명수에 따라 다른 만족도
for r in range(1, N + 1):
    for c in range(1, N + 1):
        idx = std_order.index(classroom[r - 1][c - 1]) ##std_order와 std_like를 연결하기 위한 인덱스
        like = 0 ##교실 (r, c)에 앉은 학생의 만족도

        sit = near(N, r, c) ##인접한 자리의 좌표 반환

        ##인접한 자리의 학생이, 좋아하는 학생인지 확인
        for s in sit:
            if classroom[s[0] - 1][s[1] - 1] in std_like[idx]:
                like += 1

        ##전체 학생 만족도에 (r, c) 학생의 만족도 추가
        satisfaction += sat[like]

print(satisfaction)