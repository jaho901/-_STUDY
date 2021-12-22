import sys
sys.stdin = open('1916.txt')
from heapq import heappop, heappush

N = int(input())
M = int(input())
node = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    node[u].append([w, v])
start, end = map(int, input().split())
INF = 100000000
visited = [INF] * (N+1)

def dijkstra(s):
    heap = []
    heappush(heap, [0, s])
    visited[s] = 0

    while heap:
        w, v = heappop(heap)
        
        # dijkstra에서 시간초과 났을 때 방지할 방안
        if visited[v] < w:
            continue
        
        for next_w, next_v in node[v]:
            nw = visited[v] + next_w
            if visited[next_v] > nw:
                visited[next_v] = nw
                heappush(heap, [nw, next_v])

dijkstra(start)
print(visited[end])
