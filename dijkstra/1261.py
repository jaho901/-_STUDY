import sys
sys.stdin = open('1261.txt')
from heapq import heappush, heappop

M, N = map(int, input().split())
sudo = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dijkstra():
    heap = []
    heappush(heap, [0, 0, 0])
    visited[0][0] = 1

    while heap:
        w, u, v = heappop(heap)
        if u == N-1 and v == M-1:
            print(w)
            return

        for k in range(4):
            nx, ny = u + dx[k], v + dy[k]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = 1

                if sudo[nx][ny] == 1:
                    heappush(heap, [w+1, nx, ny])
                else:
                    heappush(heap, [w, nx, ny])

dijkstra()