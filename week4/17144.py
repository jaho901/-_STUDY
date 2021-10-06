import sys
sys.stdin = open('17144.txt')

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
location = []
# 공기청정기의 위치 찾기
for i in range(R):
    if arr[i][0]==-1:
        location.append(i)
# print(location)
# 미세먼지가 퍼지는 값을 함수로 생성
# 여기서 규칙이 처음에 있는 값으로 N/5로 나눠야하는데
# 다른 미세먼지로부터 추가된 값을 합쳐서 나누면 안되기 때문에 [기존미세먼지, 추가된미세먼지]로 생성
def dust_expansion(arr):
    for i in range(R):
        for j in range(C):
            # 미세먼지가 존재하는 칸에서는
            if arr[i][j] != 0 and arr[i][j] != -1:
                cnt = 0
                # 처음에는 int값으로 존재하면서 미세먼지 크기가 5이상이어야지 N/5로 나눠진다.
                if type(arr[i][j])==int and arr[i][j] >= 5:
                    # 상하좌우로 가능한 부분에만 추가해준다.
                    for k in range(4):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                            if type(arr[nx][ny]) == int:
                                arr[nx][ny] = [arr[nx][ny], arr[i][j]//5]
                            else:
                                arr[nx][ny] = [arr[nx][ny][0], arr[nx][ny][1] + arr[i][j] // 5]
                            cnt += 1
                    arr[i][j] -= arr[i][j]//5*cnt
                # 다른 미세먼지로부터 확산되어있는 부분인 경우에는 아래와 같이 변경
                elif type(arr[i][j]) != int and arr[i][j][0] >= 5:
                    for k in range(4):
                        nx, ny = i + dx[k], j + dy[k]
                        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
                            if type(arr[nx][ny]) == int:
                                arr[nx][ny] = [arr[nx][ny], arr[i][j][0]//5]
                            else:
                                arr[nx][ny] = [arr[nx][ny][0], arr[nx][ny][1] + arr[i][j][0] // 5]
                            cnt += 1
                    arr[i][j][0] -= arr[i][j][0]//5*cnt
    
    # 마지막으로 기존미세먼지와 추가된미세먼지값들을 다 합쳐준다.
    for i in range(R):
        for j in range(C):
            if type(arr[i][j]) != int:
                arr[i][j] = arr[i][j][0] + arr[i][j][1]
    return arr

up_dx = [0, -1, 0, 1]
up_dy = [1, 0, -1, 0]
lo_dx = [0, 1, 0, -1]
lo_dy = [1, 0, -1, 0]

# 공기청정기로 인해 이동시키는 함수 생성
def air_cleaner(location):
    k = 0
    up_x = location[0]
    lo_x = location[1]
    y = 1
    up = [arr[up_x][y]]
    lo = [arr[lo_x][y]]
    arr[up_x][y] = 0
    arr[lo_x][y] = 0
    # 공기청정기 윗칸부터 회전시킴 (방향벡터로 이동)
    while True:
        nx = up_x + up_dx[k]
        ny = y + up_dy[k]
        if 0 <= nx <= location[0] and 0 <= ny < C:
            if arr[nx][ny] == -1:
                break
            else:
                up.append(arr[nx][ny])
                arr[nx][ny] = up.pop(0)
                up_x, y = nx, ny
        else:
            k = (k+1)%4
    k = 0
    y = 1
    # 공기청정기 아래칸 회전시킴 (방향벡터로 이동)
    while True:
        nx = lo_x + lo_dx[k]
        ny = y + lo_dy[k]
        if location[1] <= nx < R and 0 <= ny < C:
            if arr[nx][ny] == -1:
                break
            else:
                lo.append(arr[nx][ny])
                arr[nx][ny] = lo.pop(0)
                lo_x, y = nx, ny
        else:
            k = (k+1)%4
    return arr

# 총 T초만큼 미세먼지확산과 공기청정기 회전을 반복수행
for _ in range(T):
    arr = dust_expansion(arr)
    air_cleaner(location)

# 마지막으로 존재하는 모든 미세먼지값의 총 합을 계산
result = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != -1 and arr[i][j] != 0:
            result += arr[i][j]
print(result)
