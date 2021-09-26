import sys
sys.stdin = open('14500.txt')

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

result = 0

def te_1(x, y):
    global result
    total = []
    if y+3 < M:
        total.append(data[x][y]+data[x][y+1]+data[x][y+2]+data[x][y+3])
    if x+3 < N:
        total.append(data[x][y]+data[x+1][y]+data[x+2][y]+data[x+3][y])
    total.append(0)
    if result < max(total):
        result = max(total)
    return

def te_2(x, y):
    global result
    total = 0
    if x+1 < N and y+1 < M:
        total += data[x][y]+data[x][y+1]+data[x+1][y]+data[x+1][y+1]
    else:
        total = 0
    if result < total:
        result = total
    return

def te_3(x, y):
    global result
    total = []
    if x+1 < N and y+2 < M:
        total.append(data[x][y]+data[x][y+1]+data[x][y+2]+data[x+1][y])
        total.append(data[x][y]+data[x][y+1]+data[x][y+2]+data[x+1][y+2])
    if x+2 < N and y+1 < M:
        total.append(data[x][y]+data[x][y+1]+data[x+1][y+1]+data[x+2][y+1])
        total.append(data[x][y]+data[x+1][y]+data[x+2][y]+data[x][y+1])
    if x-1 >= 0 and y+2 < M:
        total.append(data[x][y]+data[x][y+1]+data[x][y+2]+data[x-1][y+2])
    if x+2 < N and y+1 < M:
        total.append(data[x][y]+data[x+1][y]+data[x+2][y]+data[x+2][y+1])
    if x-2 >= 0 and y+1 < M:
        total.append(data[x][y]+data[x][y+1]+data[x-1][y+1]+data[x-2][y+1])
    if x+1 < N and y+2 < M:
        total.append(data[x][y]+data[x+1][y]+data[x+1][y+1]+data[x+1][y+2])
    total.append(0)
    if result < max(total):
        result = max(total)
    return

def te_4(x, y):
    global result
    total = []
    if x+2 < N and y+1 < M:
        total.append(data[x][y]+data[x+1][y]+data[x+1][y+1]+data[x+2][y+1])
    if x-1 >= 0 and y+2 < M:
        total.append(data[x][y]+data[x][y+1]+data[x-1][y+1]+data[x-1][y+2])
    if x-2 >= 0 and y+1 < M:
        total.append(data[x][y]+data[x-1][y]+data[x-1][y+1]+data[x-2][y+1])
    if x+1 < N and y+2 < M:
        total.append(data[x][y]+data[x][y+1]+data[x+1][y+1]+data[x+1][y+2])
    total.append(0)
    if result < max(total):
        result = max(total)
    return

def te_5(x, y):
    global result
    total = []
    if y+2 < M and x+1 < N:
        total.append(data[x][y]+data[x][y+1]+data[x][y+2]+data[x+1][y+1])
    if y+2 < M and x-1 >= 0:
        total.append(data[x][y]+data[x][y+1]+data[x][y+2]+data[x-1][y+1])
    if x+2 < N and y-1 >= 0:
        total.append(data[x][y]+data[x+1][y]+data[x+2][y]+data[x+1][y-1])
    if x+2 < N and y+1 < M:
        total.append(data[x][y]+data[x+1][y]+data[x+2][y]+data[x+1][y+1])
    total.append(0)
    if result < max(total):
        result = max(total)
    return

for i in range(N):
    for j in range(M):
        te_1(i, j)
        te_2(i, j)
        te_3(i, j)
        te_4(i, j)
        te_5(i, j)

print(result)