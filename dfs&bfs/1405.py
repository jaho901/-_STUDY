import sys
sys.stdin = open('1405.txt')

data = list(map(int, input().split()))
N = data[0]
director = data[1:]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0]*(2*N+1) for _ in range(2*N+1)]
visited[N][N] = 1
result = 0

def dfs(x, y, cnt, p):
    global result

    if cnt == N:
        result += p
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if visited[nx][ny]:
            continue
        if 0 <= nx < 2*N + 1 and 0 <= ny < 2*N + 1:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, p*director[i]/100)
            visited[nx][ny] = 0
        else:
            continue

dfs(N, N, 0, 1)
print(result)
