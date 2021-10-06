import sys
# sys.stdin = open('input.txt')
# python은 느리지만 메모리가 크다
# BUT, pypy3는 빠르지만 메모리가 작다
# 그렇기 때문에 메모리초과가 난 경우에는 python으로 실행해보자!!
sys.setrecursionlimit(100000)

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# 현재 장소에서 연결되어 있는 모든 장소 방문목록에 저장
def dfs(x, y, k):
    for l in range(4):
        nx = x + dx[l]
        ny = y + dy[l]
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] > k and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, k)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 1

# 가장 큰 값을 구하고 밑에 k 반복문 range 지정
maximum = max(map(max, data))
maximum = min(maximum, 100)
# print(maximum)

# 위에서 정한 값 안에서 반복문 시행
for k in range(1, maximum+1):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if data[i][j] > k and visited[i][j] == 0:
                # 처음 방문한 지점 체크
                visited[i][j] = 1
                # 한 개의 지역 더해주기
                cnt += 1
                dfs(i, j, k)
    # 그때마다 얻어지는 결과를 계속해서 비교
    result = max(result, cnt)

print(result)
