import sys
sys.stdin = open('9370.txt')
from heapq import heappop, heappush

INF = 1000000000

def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    visited = [INF] * (n+1)
    visited[start] = 0

    while heap:
        w, v = heappop(heap)
        for nw, nv in node[v]:
            if visited[nv] > w + nw:
                visited[nv] = w + nw
                heappush(heap, [w+nw, nv])
    return visited

T = int(input())
for tc in range(1, T+1):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    node = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        node[a].append([d, b])
        node[b].append([d, a])
    object = []
    for _ in range(t):
        object.append(int(input()))
        
    road_s = dijkstra(s)
    road_g = dijkstra(g)
    road_h = dijkstra(h)

    result = []
    for i in object:
        if road_s[i] == road_s[g] + road_g[h] + road_h[i] or road_s[i] == road_s[h] + road_h[g] + road_g[i]:
            result.append(i)
    result = sorted(result)
    print(*result)
