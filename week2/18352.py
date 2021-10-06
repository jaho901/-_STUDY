# deque 받아오기
from collections import deque

# 큐를 사용한 bfs 실행
def bfs(x, k):
    # 큐 생성
    queue = deque()
    # 현재 위치 방문
    visited[x] = 1
    queue.append(x)
    # value는 k가 바뀜을 알기위해 지정
    value = 0
    # 최단거리가 K로 지정될때까지 돌림
    while k > 0:
        # 처음 부모노드 제거
        x = queue.popleft()
        # 그 부모노드와 연결된 모든 자식노드 추가
        for j in arr[x]:
            if visited[j] == 0:
                queue.append(j)
                visited[j] = 1
        # 큐가 비어있으면 멈추고
        if not queue:
            break
        # value가 큐에 존재하면 넘어가고
        if value in queue:
            pass
        # value가 큐에 없으면 k를 바꿔준다.
        else:
            value = queue[-1]
            k -= 1
    return queue

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
visited = [1] + [0]*N
result = bfs(X, K)
result = sorted(result)
if result:
    for i in result:
        print(i)
else:
    print(-1)