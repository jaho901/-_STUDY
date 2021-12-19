import sys
sys.stdin = open('1743.txt')
from collections import deque

n, m, k = map(int, input().split())
trash = [[0]*m for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    trash[x-1][y-1] = 1
visited = [[False]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = 0

def bfs():
    global result

    for i in range(n):
        for j in range(m):
            ans = 0

            if visited[i][j] != False:
                continue

            else:
                if trash[i][j] == 1:
                    visited[i][j] = True
                    ans += 1
                    queue = deque()
                    queue.append([i, j])
                    while queue:
                        x, y = queue.popleft()

                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < n and 0 <= ny < m and trash[nx][ny] == 1 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                ans += 1
                                queue.append([nx, ny])
                    result = max(result, ans)

bfs()
print(result)
