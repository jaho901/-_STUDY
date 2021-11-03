import sys
sys.stdin = open('10282.txt')
from heapq import heappop, heappush

T = int(input())
for tc in range(1, T+1):
    n, d, s = map(int, input().split())
    computer = [[] for _ in range(n+1)]
    # 노드 리스트 생성
    for _ in range(d):
        a, b, time = map(int, input().split())
        computer[b].append([time, a])

    INF = 100000000
    # 시간 넣을 visited 리스트 생성
    visited = [INF] * (n+1)
    # 힙큐 생성
    heap = []

    # 다익스트라는 로직 동일
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
    # 감염된 컴퓨터 수
    com_num = 0
    # 감염되기까지 걸리는 최대 시간
    com_time = 0
    for i in visited:
        if i != INF:
            com_num += 1
            if com_time < i:
                com_time = i
    print(com_num, com_time)
