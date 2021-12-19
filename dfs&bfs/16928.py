import sys
sys.stdin = open('16928.txt')
from collections import deque

n, m = map(int, input().split())
visited = [False]*101
ladder = [0]*101
snake = [0]*101
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

result = 101

def bfs():
    global result

    queue = deque()
    queue.append([1, 0])
    visited[1] = True

    while queue:
        start = queue.popleft()

        if start[0] == 100:
            result = min(result, start[1])
            continue

        for i in range(1, 7):
            end = start[0] + i
            if end <= 100:
                if visited[end] == True:
                    continue

                visited[end] = True

                if ladder[end] != 0:
                    end = ladder[end]
                if snake[end] != 0:
                    end = snake[end]

                queue.append([end, start[1]+1])
bfs()
print(result)

