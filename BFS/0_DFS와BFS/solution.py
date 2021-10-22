"""

BAEKJOON 1260번 : DFS와 BFS

"""

N, M, v = map(int, input().split())

graph = {}

for m in range(M):
    a, b = map(int, input().split())

    if a not in graph.keys():
        ##새로운 노드
        graph[a] = [b]
    else:
        #기존에 있는 노드
        graph[a].append(b)
        graph[a].sort()

    if b not in graph.keys():
        ##새로운 노드
        graph[b] = [a]
    else:
        #기존에 있는 노드
        graph[b].append(a)
        graph[b].sort()

visited = []
key = list(graph.keys())
i = 0
while len(visited) != len(key):
    if graph[v]:
        pass

