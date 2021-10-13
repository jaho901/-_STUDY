import sys
sys.stdin = open('11404.txt')
from heapq import heappush, heappop

# 가장 큰 수를 INF로 저장
INF = 100000000
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
bus = [[] for _ in range(N+1)]
# bus에서 a인덱스에 [비용, 도착지점] 순으로 추가해주었다.
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    bus[a].append([c, b])
# print(bus)
# 결과를 넣을 결과리스트
result = []

# 다익스트라 알고리즘 사용
def dijkstra(start):
    # 1. heapq 생성
    heap = []
    # 2. 초기값 지정 및 방문처리(+ 자기 위치 0)
    heappush(heap, [0, start])
    visited = [INF] * (N+1)
    visited[start] = 0
    # 3. while문을 통해 시작점에서 이동가능한 모든 지점 추가
    while heap:
        c, b = heappop(heap)

        for next_c, next_b in bus[b]:
            # 전 위치까지의 비용과 새로운 비용 합
            money = next_c + c
            if money < visited[next_b]:
                visited[next_b] = money
                # 여기서 중요한게 money를 push해줘야한다!!
                heappush(heap, [money, next_b])
    # 또한, 하나의 조건이 이동 불가능한 지역은 0으로 표시
    # 즉, 전 지역에서 INF가 존재하면 0으로 바꿔준다.
    for i in range(len(visited)):
        if visited[i] == INF:
            visited[i] = 0
    return visited[1:]

# 한 줄씩 다익스트라 알고리즘을 사용해
# 1번 도시에서 ~~~
# 2번 도시에서 ~~~
# ...
# 마지막 도시에서 ~~~
# 의 결과를 각각 구해서 하나의 리스트들을 계속해서 result에 추가
for i in range(1, N+1):
    result.append(dijkstra(i))
for i in result:
    print(*i)
# print(result)