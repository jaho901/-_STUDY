import sys
sys.stdin = open('1932.txt')

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
max_ans = 0

# 뒤에서부터 탐구해줄 dp 어레이 생성
dp = [[0]*i for i in range(1, N+1)]
# 시작점 지정
dp[0][0] = triangle[0][0]
# 반복문을 통해 뒤에서부터 탐구시작
for i in range(1, N):
    for j in range(i+1):
        # 위에서 갈 수 있는 방법은 2가지
        left, right = j-1, j
        if left < 0:
            left = 0
        elif right == i:
            right -= 1
        # 올라가면서 계속해서 추가해준다.
        dp[i][j] = triangle[i][j] + max(dp[i-1][left], dp[i-1][right])
print(max(dp[N-1]))

'''
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]


def dfs(cur, total, i):
    global result

    if cur == N:
        if total > result:
            result = total
        return

    dfs(cur+1, total+data[cur][i], i)
    dfs(cur+1, total+data[cur][i+1], i+1)


result = 7
dfs(1, result, 0)
print(result)
'''