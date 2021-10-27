import sys
sys.stdin = open('10282.txt')
from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    n, d, s = map(int, input().split())

    computer = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, time = map(int, input().split())
        computer[b].append([time, a])

    INF = 100000000
    visited = [INF] * (n+1)
    heap = []

    def dijkstra(s):
        heappush(heap, [0, s])
        visited[s] = 0

        while heap:
            time, v = heappop(heap)

            for next_time, next_v in computer[v]:
                nt = next_time + time
                if visited[next_v] > visited[v] + next_time:
                    visited[next_v] = nt
                    heappush(heap, [nt, next_v])


    dijkstra(s)
    com_num = 0
    com_time = 0
    for i in visited:
        if i != INF:
            com_num += 1
            if com_time < i:
                com_time = i
    print(com_num, com_time)
