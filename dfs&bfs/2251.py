import sys
sys.stdin = open('2251.txt')
from collections import deque

'''
0 0 10
->
0 0 10 
0 9 1 (z -> y)
8 0 2 (z -> x) -> 0 8 2 (x -> y)
8 2 0 -> 0 2 8 (x -> z)
1 9 0 -> 1 0 9 (y -> z) -> 0 1 9
(y -> x)
'''

a, b, c = map(int, input().split())

queue = deque()
queue.append([0, 0])

visited = [[0]*(b+1) for _ in range(a+1)]
visited[0][0] = 1

result = []

def change(a, b):
    if visited[a][b] == 0:
        visited[a][b] = 1
        queue.append([a, b])

def bfs():

    while queue:
        x, y = queue.popleft()
        # 남아있는 c에 들어있는 물의 양 = z
        z = c - x - y

        # x = 0인 경우의 z값을 result에 저장
        if x == 0:
            result.append(z)

        # x -> y
        sub = min(x, b-y)
        change(x-sub, y+sub)

        # x -> z
        sub = min(x, c-z)
        change(x-sub, y)

        # y -> x
        sub = min(a-x, y)
        change(x+sub, y-sub)

        # y -> z
        sub = min(y, c-z)
        change(x, y-sub)

        # z -> x
        sub = min(a-x, z)
        change(x+sub, y)

        # z -> y
        sub = min(b-y, z)
        change(x, y+sub)

bfs()
result = sorted(result)
print(*result)