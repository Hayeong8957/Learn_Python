# 그래프 알고리즘

## 최소 신장 트리(MST)

- 하나의 연결성분으로 이루어진 무방향 가중치 그래프에서 간선의 가중치의 합이 최소인 신장 트리
- 최소 신장 트리(MST)를 찾는 대표적인 알고리즘: Kruskal, prim

### Kruskal(크루스칼) 알고리즘

1. 간선 데이터를 가중치에 따라 오름차순으로 정렬 > 간선리스트 L만듦
2. while 트리의 간선 수 < N-1:
   1. L에서 가장 작은 가중치를 가진 간선 e를 가져오고, e를 L에서 제거
   2. if 간선 e가 T에 추가하여 싸이클을 만들지 않으면:
      1. 간선 e를 T에 추가
3. 모든 간선에 대해 2번의 과정을 반복

- 사이클이 발생하는 경우 판단 > union-find 연산 실행
  - **union(자식노드, 루트노드)**, **find(자식노드) = 루트노드**

### prim 알고리즘

1. D를 최대로 초기화. 시작 정점 s의 D[s] = 0
   1. D → **최소의 가중치 값이 계속 저장**이 됨, 현재 시점에서의 연결된 가중치 값
2. while T의 정점 수 < N:
   1. T에 속하지 않은 각 정점 i에 대해 D[i]가 최소인 정점, min_vertex를 찾아 T에 추가
      → 방문한 정점으로 취급(그래프 탐색 알고리즘 → 최소 정점과 연결되어 있는 간선의 가중치 값을 다시 계산)
   2. for T에 속하지 않은 각 정점 w에 대해서: → 아직 방문 X 정점들에 대해서

      1. if 간선 (min_vertex, w)의 가중치 < D[w]:
      2. D[w] = 간선(min_vertex, w)의 가중치

      → 현재 min_vertex와 연결된 정점의 간선의 값이 최소인지, 이전에 저장되어 있는 간선의 가중치 값이 더 적은지 비교한 후 업데이트. (if → false → 값 갱신X)

## 최단 경로 알고리즘(Dijkstra)

- 출발점이 주어짐, 출발점 ~ 각 정점까지의 최단 거리
- D → 출발점으로부터 각 정점까지의 경로의 길이 저장

1. D를 최대로 초기화. 시작 정점 s의 D[s] = 0
   1. D → 간선의 최솟값에 대한 저장
2. for k in range(N):
   1. 방문 안 된 각 정점 i에 대해 D[i]가 최소인 정점 min_vertex를 찾고 방문
   2. for min_vertex에 인접한 각 정점 w에 대해서:
      1. if w 가 방문 안 된 정점이면
         1. if D[min_vertex] + wt < D[w] → D[w] = D[min_vertex] + wt
            → wt = 간선 (min_vertex, w)의 가중치
            → min_vertex를 경유해 정점 w까지의 거리 < 현재의 D[w]
            → D[w]를 D[min_vertex] + wt로 갱싱
         2. previous[w] = min_vertex
