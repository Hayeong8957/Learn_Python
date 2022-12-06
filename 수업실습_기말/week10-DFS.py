# 인접리스트 dfs
def dfs(v):
    visited[v] = True # 정점 v 방문
    print(v) # 정점 v 출력
    adj_list[v].sort()
    for w in adj_list[v]: # 정점 v에 인접한 각 정점에 대해
        if not visited[w]:
            dfs(w) # v에 인접한 방문 안된 정점 재귀호출

ver, edge, s = map(int, input().split())
# 빈 인접리스트 구조 생성
adj_list = [[-1]] + [[] for _ in range(ver)]
N = len(adj_list)
visited = [None] * N

# m줄만큼 input받기 => 간선 정보
# 쌍방향이므로 append를 사용하여 간선과 정점 연결
for x in range(edge):
    edge_a, edge_b = map(int, input().split())
    adj_list[edge_a].append(edge_b)
    adj_list[edge_b].append(edge_a)
print("[DFS 방문순서]")
dfs(s)

