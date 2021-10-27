import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush

N, M, X = map(int, input().split())
node = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, t = map(int, input().split())
    node[u].append([t, v])

INF = 100000000
heap = []

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

for i in range(1, N+1):
    visited = [INF] * (N + 1)
    dijkstra(i)
    a = visited[X]
    visited = [INF] * (N + 1)
    dijkstra(X)
    b = visited[i]
    total = a + b
    if result < total:
        result = total
        
print(result)