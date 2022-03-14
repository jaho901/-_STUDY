import sys
sys.stdin = open('2667.txt')
from collections import deque

n = int(input())
data = [list(map(int, input())) for _ in range(n)]

result = []

def bfs(x, y):
    global data, result
    if data[x][y] == 0:
        return
    else:
        data[x][y] = 0
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        sub = 1
        queue = deque()
        queue.append([x, y])
        while queue:
            i, j = queue.popleft()
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0 <= nx < n and 0 <= ny < n and data[nx][ny]:
                    queue.append([nx, ny])
                    data[nx][ny] = 0
                    sub += 1
                else:
                    pass
        result.append(sub)
        return

for i in range(n):
    for j in range(n):
        bfs(i, j)
result = sorted(result)
print(len(result))
for x in result:
    print(x)