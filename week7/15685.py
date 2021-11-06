import sys
sys.stdin = open('input.txt')

'''
x,y 시작점 / d 시작방향 / g 세대
0: 오른쪽 / 1: 위쪽 / 2: 왼쪽 / 3: 아래쪽
3301
4213
4221
'''

N = int(input())
data = [[0]*102 for _ in range(102)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    data[y][x] = 1
    direction = [d]

    for _ in range(g):
        sub = []
        for i in range(len(direction)):
            sub.append((direction[-(i+1)]+1)%4)
        direction.extend(sub)

    for k in range(len(direction)):
        nx, ny = x+dx[direction[k]], y+dy[direction[k]]
        data[ny][nx] = 1
        x, y = nx, ny

result = 0

for i in range(102):
    for j in range(102):
        if data[i][j] == 1:
            if data[i+1][j] == 1 and data[i][j+1] == 1 and data[i+1][j+1] == 1:
                result += 1

print(result)


