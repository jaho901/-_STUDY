import sys
sys.stdin = open('10971.txt')

N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*N

def dfs(cur, total, start, s):
    global result

    if cur == N-1:
        if city[s][start] != 0:
            total += city[s][start]
            if result > total:
                result = total
            return

    for i in range(N):
        if city[s][i] != 0 and not visited[i]:
            visited[i] = 1
            dfs(cur+1, total+city[s][i], start, i)
            visited[i] = 0

result = 1000000000

for i in range(N):
    visited[i] = 1
    dfs(0, 0, i, i)
    visited[i] = 0

print(result)