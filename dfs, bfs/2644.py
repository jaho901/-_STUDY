import sys
sys.stdin = open('2644.txt')

n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [0] * (n+1)
visited[a] = 1
result = -1

def dfs(a):
    global result
    # 도착하면 result가 0보다 큰 값을 가지니깐 종료
    if result > 0:
        return
    # 도착하면 result값을 새로 지정
    if a == b:
        result = visited.count(1) - 1
        return
    # a라는 노드에서 이동 할 수 있는 모든 노드로 이동
    # 방문목록 변경해주면서 이동하고 만약에 b를 못만나면 다시 방문목록 초기화
    for idx in arr[a]:
        if visited[idx] == 0:
            visited[idx] = 1
            dfs(idx)
            visited[idx] = 0
    return

dfs(a)
# 어차피 못만나면 result값이 변경이 안되므로 -1이 나오고
# 만난다면 result값이 변경되어 원하는 값을 얻을 수 있다.
print(result)
