"""

BAEKJOON 21609번 : 상어 중학교

"""

def findBlockGroup(block):
    group = []
    visited = []

    tmp_group = []
    color = None
    for r in range(len(block)):
        for c in range(len(block[r])):
            ##방문기록이 없는 block에만 방문
            if (r, c) not in visited:
                if color:
                    ##none이 아닌 경우
                    pass
                else:
                    ##none인 경우 - 무지개 or 첫번째 일반 블록
                    pass


                visited.append((r, c))









    return group


##90도 반시계 방향으로 회전시킨 게임판을 반환
def rotate(game):
    answer = []

    return answer

N, M = map(int, input().split())
block = []

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for n in range(N):
    line = list(map(int, input().split()))
    block.append(line)

findBlockGroup(block)


