import sys
sys.stdin = open('2660.txt')

'''
#플로이드 와샬
# k : 경유지
for k in range(1, v+1):
    # i : 출발지    
    for i in range(1, v+1):
        # j : 목적지
        for j in range(1, v+1):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
'''

N = int(input())
INF = 999999999
node = [[INF]*(N+1) for _ in range(N+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        node[a][b]= 1
        node[b][a] = 1

for i in range(1, N+1):
    node[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            node[i][j] = min(node[i][j], node[i][k]+node[k][j])

for aa in node:
    print(aa)

result = []
for x in range(1, N+1):
    result.append(max(node[x][1:]))

min_result = min(result)
# 가장 작은 점수 및 그 점수를 가지고 있는 인원 수
print(min_result, result.count(min_result))

answer = []
for i in range(len(result)):
    if result[i] == min_result:
        answer.append(i+1)

answer = sorted(answer)
print(*answer)
