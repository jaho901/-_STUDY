import sys
sys.stdin = open('16927.txt')

N, M, R = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

num = min(N, M)
num = num//2

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def turn(data, R):
    mydata = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    i, j = 0, 0
    t = 0
    k = 0
    numbers = []

    while True:
        while True:
            ni, nj = i+dx[k], j+dy[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if ni == t or nj == t or ni == N-1-t or nj == M-1-t:
                    numbers.append(data[i][j])
                    i,j = ni, nj
            else:
                k = (k+1)%4

            if i == t and j == t:
                break

        if R % len(numbers) == 0:
            r = numbers.pop(0)
            numbers.append(r)
        else:
            for _ in range((R % len(numbers))-1):
                r = numbers.pop()
                numbers.insert(0, r)

        k = 0

        while True:
            ni, nj = i + dx[k], j + dy[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if ni == t or nj == t or ni == N-1-t or nj == M-1-t:
                    visited[ni][nj] = True
                    mydata[ni][nj] = numbers.pop(0)
                    i,j = ni, nj
            else:
                k = (k+1)%4

            if i == t and j == t:
                break

        t += 1
        i, j = t, t
        k = 0
        numbers = []

        if t == num:
            if N % 2 == 1 and M % 2 == 1:
                mydata[N//2][M//2] = data[N//2][M//2]
            return mydata

d = turn(data, R)
for row in d:
    print(*row)



        

