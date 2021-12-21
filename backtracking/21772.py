import sys
sys.stdin = open('21772.txt')

'''
가희 : 1초마다 상하좌우 중 한 방향으로 1번 이동 or 이동하지않고 머문다.
이동한 지점에 고구마 있다 => 고구마 먹는다 (시간소요X)
고구마 먹으면 다시는 그 자리에 생기지 않는다.

T초 이동 시 최대한 많이 먹고 싶다.

'''

R, C, T = map(int, input().split())
data = [list(input()) for _ in range(R)]

pos_x, pos_y = 0, 0
for i in range(R):
    for j in range(C):
        if data[i][j] == 'G':
            pos_x = i
            pos_y = j
data[pos_x][pos_y] = '.'
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = 0


def dfs(x, y, sweet_potato, cnt):
    global result

    if cnt == T:
        result = max(result, sweet_potato)
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if data[nx][ny] == '#':
                continue

            elif data[nx][ny] == 'S':
                data[nx][ny] = '.'
                dfs(nx, ny, sweet_potato+1, cnt+1)
                data[nx][ny] = 'S'

            elif data[nx][ny] == '.':
                dfs(nx, ny, sweet_potato, cnt+1)


dfs(pos_x, pos_y, 0, 0)
print(result)