import sys
sys.stdin = open('7576.txt')
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 큐 생성
queue = deque()
# 모든 토마토의 위치 큐에 담기!
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i, j])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0

while queue:
    x, y = queue.popleft()
    # 현재 큐의 위치에서 4가지 방향으로 이동하면서 토마토 확산
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            queue.append([nx, ny])
            # 바로 전위치에서 1씩 추가하면 가장 최댓값 구할 수 있음
            arr[nx][ny] = arr[x][y] + 1


exist = True
for i in range(N):
    for j in range(M):
        # 모든 토마토 확산 이후에도 0이 남아있으면 -1 출력
        if arr[i][j] == 0:
            print(-1)
            exist = False
            break
    if not exist:
        break
    # 아닌 경우네는 max값을 출력
    cnt = max(cnt, max(arr[i]))
if exist:
    print(cnt-1)