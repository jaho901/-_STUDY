import sys
sys.stdin = open('2178.txt')
from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    # 큐 생성
    queue = deque()
    # 방문목록 저장(저장하는 값을 이동횟수로 저장한다!!)
    visited[x][y] = 1
    # 현재 위치를 큐에 추가
    queue.append((x, y))
    while queue:
        # 선입선출형식으로 x, y값을 큐에서 제거하면서 저장
        x, y = queue.popleft()
        # 현재위치에서 상하좌우 중에 이동가능한 부분 전부 큐에 추가
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                # 이동하는 지점에는 현재위치 + 1의 값을 저장해준다!
                visited[nx][ny] += visited[x][y] + 1

    return visited[N-1][M-1]

print(bfs(0, 0))
