import sys
sys.stdin = open('15685.txt')

'''
x,y 시작점 / d 시작방향 / g 세대
0: 오른쪽 / 1: 위쪽 / 2: 왼쪽 / 3: 아래쪽
3301
4213
4221

3301 => [0, 1세대] => [0, 1]
4213 => [1, 3세대] => [1, 2] -> [1, 2, 3, 2] -> [1, 2, 3, 2, 3, 0, 3, 2]
4221 => [2, 1세대] => [2, 3]
규칙 : 뒤에서부터 1씩 더하면서 추가하기

'''

N = int(input())
data = [[0]*102 for _ in range(102)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    # 처음 시작점 체크
    data[y][x] = 1
    direction = [d]

    # 각각의 세대 만큼 하나의 규칙을 만들고 그 규칙을 direction에 담는다.
    for _ in range(g):
        sub = []
        for i in range(len(direction)):
            sub.append((direction[-(i+1)]+1)%4)
        direction.extend(sub)
    
    # 그 위치순으로 모두 1로 변경해주기
    for k in range(len(direction)):
        nx, ny = x+dx[direction[k]], y+dy[direction[k]]
        data[ny][nx] = 1
        x, y = nx, ny

result = 0

# 모든 위치에서 살피면서 4꼭지점에 1이 있으면 결과 result를 1씩 추가해준다.
for i in range(102):
    for j in range(102):
        if data[i][j] == 1:
            if data[i+1][j] == 1 and data[i][j+1] == 1 and data[i+1][j+1] == 1:
                result += 1

print(result)


