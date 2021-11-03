import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

N, M, X = map(int, input().split())
node = [[] for _ in range(N+1)]
# 노드리스트 생성
for _ in range(M):
    u, v, t = map(int, input().split())
    node[u].append([t, v])

INF = 100000000
heap = []

# 다익스트라 로직은 동일
def dijkstra(s):
    heappush(heap, [0, s])
    visited[s] = 0

    while heap:
        t, v = heappop(heap)

        for nt, nv in node[v]:
            time = t + nt
            if visited[nv] > visited[v] + nt:
                visited[nv] = time
                heappush(heap, [time, nv])

result = 0

# 각각의 학생들 모두 반복문 실시
for i in range(1, N+1):
    # 집에서 목적지까지 출발
    visited = [INF] * (N + 1)
    dijkstra(i)
    a = visited[X]
    # 목적지에서 집까지 출발
    visited = [INF] * (N + 1)
    dijkstra(X)
    b = visited[i]
    # 각각의 값을 더한 total의 최솟값을 result에 저장
    total = a + b
    if result < total:
        result = total
        
print(result)