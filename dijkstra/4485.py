import sys
sys.stdin = open('4485.txt')
from heapq import heappop, heappush

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijkstra(num):
    heap = []
    heappush(heap, [cave[0][0], 0, 0])
    visited[0][0] = 1

    while heap:
        rupee, x, y = heappop(heap)

        if x == n-1 and y == n-1:
            print('Problem {}: {}'.format(num, rupee))
            break

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = 1
                heappush(heap, [rupee+cave[nx][ny], nx, ny])

num = 1
while True:
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    visited = list([0]*n for _ in range(n))
    dijkstra(num)
    num += 1
