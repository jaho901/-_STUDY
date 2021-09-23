import sys
sys.stdin = open('14502.txt')
from collections import deque
import copy

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    global ans
    # i와 j값마다 계속해서 data를 변경해줘야하기 때문에 deepcopy 사용!!
    # 리스트를 복사하면 slicing이나 list()를 사용하면 되는데
    # array를 복사하기 때문에 deepcopy를 사용한다!!
    mydata = copy.deepcopy(data)
    queue = deque()
    for i in range(N):
        for j in range(M):
            # 모든 바이러스의 위치를 큐에 삽입
            if mydata[i][j] == 2:
                queue.append([i, j])
    
    while queue:
        # 그 위치를 기준으로 벽에 막히기 전까지의 모든 0을 2로 만들어준다.
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and mydata[nx][ny] == 0:
                mydata[nx][ny] = 2
                queue.append([nx, ny])
    
    cnt = 0
    # 그 이후 0의 개수를 반환한다!!
    for i in mydata:
        cnt += i.count(0)
    ans = max(ans, cnt)

# 이 함수는 N x M에서 랜덤하게 벽을 3개 세운다음에
# 계속해서 bfs()를 통해 최댓값을 구해주는 함수이다!!
def wall(x):
    # 벽이 3개 세워지면 0의 최대 개수 구하고 return
    if x == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                wall(x + 1)
                data[i][j] = 0

ans = 0
# 벽의 개수는 항상 0부터 시작
wall(0)
# 결과 출력
print(ans)
