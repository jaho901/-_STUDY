import sys
sys.stdin = open('2665.txt')
from heapq import heappop, heappush

N = int(input())
data = [list(map(int, input())) for _ in range(N)]

def dijkstra(x, y):
    heap = []
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    visited = [[0]*N for _ in range(N)]
    heappush(heap, (0, x, y))
    visited[y][x] = 1
    while heap:
        weight, nx, ny = heappop(heap)

        # heapq니깐 가장 먼저 나오는 결과가 최솟값이다!
        if nx == N-1 and ny == N-1:
            return weight

        for k in range(4):
            newx, newy = nx + dx[k], ny + dy[k]
            if 0 <= newx < N and 0 <= newy < N and visited[newx][newy] == 0:
                visited[newx][newy] = 1
                if data[newx][newy] == 1:
                    heappush(heap, (weight, newx, newy))
                # 검은 벽인 경우 weight 1 추가
                else:
                    heappush(heap, (weight+1, newx, newy))

result = dijkstra(0, 0)
print(result)