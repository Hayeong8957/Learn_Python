# 이코테
# from collections import deque
# graph = [[], [2, 3, 8], [1, 7], [1, 4, 5] ,
#          [3, 5], [3, 4], [7], [2,6,8], [1,7]]
#
# visited = [False] * 9
# bfs(graph, 1, visited)
# def bfs(graph, start, visited) :
#     # 큐 구현을 위해 deque라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문처리
#     visited[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력
#         v = queue.popleft()
#         print(v, end=" ")
#         # 아직 방문하지 않은 인접한 원소들 큐에 삽입
#         for i in graph[v] :
#             if not visited[i] :
#                 queue.append(i)
#                 visited[i] = True
#

# 수업자료
adj_list = [[2, 1], [3, 0], [3,0], [9, 8, 2, 1],
            [5], [7, 6, 4], [7,5], [6,5], [3], [3]]
N = len(adj_list)
visited = [None] * N

def bfs(i) :
    queue = []
    visited[i] = True
    queue.append(i)
    while len(queue) != 0 :
        v = queue.pop(0)
        print(v, " ", end="")
        for w in adj_list[v] :
            if not visited[w] :
                visited[w] = True
                queue.append(w)
print("BFS 방문순서:")
for i in range(N) :
    if not visited[i] :
        bfs(i)