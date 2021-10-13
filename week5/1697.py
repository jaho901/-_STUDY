import sys
sys.stdin = open('1697.txt')
from collections import deque

'''
문제를 보자마자
현재위치에서 갈 수 있는 방법이
x-1, x+1, 2x로
총 3가지 방법이 있음을 알 수 있어야하고,
그 3가지 방법으로 동시에 이동하는
bfs 방법을 선택해야함을 알아야 한다!!
'''

N, K = map(int, input().split())
# 최댓값 생성
maximum = 100000
# 방문처리
visited = [0]*(maximum+1)

def bfs():
    # 큐 생성
    queue = deque()
    queue.append(N)
    while queue:
        # deque를 통해 원래 O(n)의 시간순서를 O(0)의 시간으로 줄 일 수 있다!!
        x = queue.popleft()
        # 만약 우리가 원하는 위치에 도착했을 때 지금까지 걸린 횟수를 바로 출력하고 함수 종료
        if x == K:
            print(visited[x])
            break

        # 순서를 x-1, x+1, 2*x 순으로 지정을 해줘야지 가능!!
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= maximum and not visited[nx]:
              queue.append(nx)
              visited[nx] = visited[x] + 1

bfs()