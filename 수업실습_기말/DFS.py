# 이코테 강의
# graph = [[], [2, 3, 8], [1, 7], [1, 4, 5] ,
#          [3, 5], [3, 4], [7], [2,6,8], [1,7]]
# visited = [False] * 9
# dfs(graph, 1, visited)
# def dfs(graph, v, visited) :
#     # 현재 노드 방문처리
#     visited[v] = True
#     print(v, end=" ")
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v] :
#         if not visited[i] :
#             dfs(graph, i, visited)

# 수업자료
adj_list = [[2, 1], [3, 0], [3,0], [9, 8, 2, 1],
            [5], [7, 6, 4], [7,5], [6,5], [3], [3]]
N = len(adj_list)
visited = [None] * N

def dfs(v) :
    visited[v] = True
    print(v, " ", end="")
    for w in adj_list[v] :
        if not visited[w] :
            dfs(w)

print("DFS 방문 순서: ")
for i in range(N) :
    if not visited[i] :
        dfs(i)
