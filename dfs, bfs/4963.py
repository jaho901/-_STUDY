import sys
sys.stdin = open('4963.txt')

def recur(cur, i, j):
    data[i][j] = 0

    for k in range(8):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < h and 0 <= ny < w and data[nx][ny] == 1 :
            recur(cur+1, nx, ny)


dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

while True:
    w, h = map(int, input().split())
    ans = 0
    if w == 0 and h == 0:
        break
    else:
        if h == 1:
            data = list(map(int, input()))
            if data[0] == 0:
                print(0)
            else:
                print(1)

        else:
            data = [list(map(int, input().split())) for _ in range(h)]
            # print(data)
            for x in range(h):
                for y in range(w):
                    if data[x][y] == 1:
                        recur(0, x, y)
                        ans += 1
            print(ans)