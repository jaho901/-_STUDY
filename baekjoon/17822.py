import sys
sys.stdin = open('17822.txt')
from collections import deque

n, m, t = map(int, input().split())
onepan = []
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
17132665
def remove_dup(remove_list):
    # 인접 중복 제거
    sub_list = []
    for i in range(n):
        for j in range(m):
            if onepan[i][j] != 0:
                sub_list = [[i, j]]
                a, b = i, j
                nk = 0
                while nk < 4:
                    nx, ny = a+dx[nk], (b+dy[nk])%m
                    if 0 <= nx < n and onepan[nx][ny] != 0 and onepan[i][j] == onepan[nx][ny]:
                        sub_list.append([nx,ny])
                        a, b = nx, ny
                    else:
                        nk += 1
                        a, b = i, j
            if len(sub_list) > 1:
                for i_list in sub_list:
                    if i_list not in remove_list:
                        remove_list.append(i_list)
    return remove_list

def change(onepan):
    # 같은 수가 없는 경우 지정
    nums = []
    for i in range(n):
        for j in range(m):
            if onepan[i][j] != 0:
                nums.append(onepan[i][j])
    avg = sum(nums)/len(nums)

    for i in range(n):
        for j in range(m):
            if onepan[i][j] != 0 and onepan[i][j] > avg:
                onepan[i][j] -= 1
            elif onepan[i][j] != 0 and onepan[i][j] < avg:
                onepan[i][j] += 1
    return onepan


for i in range(n):
    queue = list(map(int, input().split()))
    queue = deque(queue)
    onepan.append(queue)

for i in range(t):
    x, d, k = map(int, input().split())
    while True:
        if d == 0:
            sub = onepan[x-1]
            sub.rotate(k)
            onepan[x-1] = sub
        else:
            sub = onepan[x-1]
            sub.rotate(-k)
            onepan[x-1] = sub
        x += x
        if x > n:
            break
    remove_list = []
    remove_list = remove_dup(remove_list)
    for w, z in remove_list:
        onepan[w][z] = 0
    if len(remove_list) == 0:
        onepan = change(onepan)
    summation = sum(map(sum, onepan))
    if summation == 0:
        break
result = sum(map(sum, onepan))
print(result)
