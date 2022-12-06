# 인접행렬 bfs
def bfs(i):
    queue = [] # 큐 선언 (리스트로 큐 구현)
    visited[i] = True
    queue.append(i) # 큐에 시작정점 삽입
    while len(queue) != 0:
        v = queue.pop(0) # 큐에서 정점 v를 가져옴
        print(v) # 정점 v 출력
        for w in range(len(matrix[v])): # 정점 v에 인접한 방문 안된 정점에 대해
            if matrix[v][w] == 1 and not visited[w] :
                visited[w] = True
                queue.append(w) # v에 인접한 정점을 큐에 삽입

ver, edge, s = map(int, input().split())
# 빈 인접 행렬 구조 생성
# 1. 0으로 matrix 초기화,
# 2. 노드의 인덱스가 1부터 시작하기 때문에 matrix의 크기를 각각 1씩 추가
matrix = [[0] * (ver+1) for _ in range(ver+1)]
N = len(matrix)
visited = [None] * N

# edge줄만큼 input받기 => 간선 정보
for i in range(edge):
    x, y = map(int, input().split())
    matrix[x][y] = matrix[y][x] = 1

# for i in range(edge) :
#     a, b = map(int, input().split())
#     matrix[a][b] = 1
#     matrix[a][b] = 1
bfs(s)
