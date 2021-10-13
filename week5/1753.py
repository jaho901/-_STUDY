import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

'''
input() : 내장함수로 입력받기 전 prompt message를 출력
          & 입력받은 값의 개행 문자를 삭제시켜서 리턴
          ==> 시간이 sys.stdin.readline()보다 더 느리다.
          but, 삼성에서는 sys를 쓸수 없기 때문에 input()만 사용


sys.stdin.readline()은 prompt message를 인수로 받지 않는다.
백준에서는 sys사용가능하기 때문에 sys.stdin.readline()을 사용해 시간단축 가능
'''
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = 100000000
# 이동가능한 정점과 가중치를 point에 저장
point = [[] for _ in range(V+1)]
# Dijkstra Algorithm 순서
# 1. heapq 생성
heap = []
# 방문목록 저장 ( 경로가 존재하지 않은 경우 INF를 출력하기 위해 INF값으로 기본값 지정 )
visited = [INF] * (V + 1)
def bfs(k):
    # 2. 자기 자신의 위치를 0으로 지정
    visited[k] = 0
    # 처음위치 k와 가중치 0을 큐에 삽입해준다.
    # 여기서 왜 가중치, 위치순이나면 우리가 원하는 최소힙은 가중치를 기준으로하기때문에
    # 가중치가 가장 먼저 존재해야지만 구현이 가능하다!!
    heappush(heap, [0, k])
    # 3. while문을 통해 시작점에서 갈 수 있는 모든 경로 큐에 추가
    while heap:
        # 처음 위치에서 갈 수 있는 정점 v와 가중치 w
        w, v = heappop(heap)
        # v에서 갈 수 있는 다음 정점 next_v와 가중치 nw를 순서대로 큐에 저장
        for nw, next_v in point[v]:
            # 가중치는 계속해서 전에 존재하던 가중치에서 더해져야함
            next_w = w + nw
            # 새로운 가중치값이 원래값보다 작은경우 변경시켜줌
            if next_w < visited[next_v]:
                visited[next_v] = next_w
                # 4. 아래의 방법을 통해 모든 새로운 경로가 추가되면 자연스럽게 가장 왼쪽에 작은 거리부터 채워진다.
                heappush(heap, [next_w, next_v])

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    # 왜 v, w순이 아닌 w, v순으로 했는지는 위에 함수로!!
    point[u].append([w, v])
bfs(K)
for i in visited[1:]:
    print(i if i != INF else "INF")




## dfs (시간초과)
'''
import sys
sys.stdin = open('1753.txt')
sys.setrecursionlimit(100000)

V, E = map(int, input().split())
K = int(input())
point = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    point[u].append([v, w])
N = len(point[K])

def dfs(cur, total, num):
    global result
    if cur == num:
        result = min(result, total)
        return

    if result < total:
        return

    for i in range(len(point[cur])):
        total += point[cur][i][1]
        dfs(point[cur][i][0], total, num)
        total -= point[cur][i][1]

for j in range(1, V+1):
    result = 300001
    dfs(K, 0, j)
    if result == 300001:
        print('INF')
    else:
        print(result)
'''