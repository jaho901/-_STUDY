import sys
sys.stdin = open('1074.txt')

N, r, c = map(int, input().split())
cnt = 0

def z(x, y, N):
    global cnt
    # 우리가 원하는 위치에 도달하면 그때의 cnt값을 보여주면서 함수 종료
    if x == r and y == c:
        print(int(cnt))
        exit(0)
    
    # 1칸까지 남게된다면 1씩 추가
    if N == 1:
        cnt += 1
        return

    # 4등분한 조각에서 만약 우리가 원하는 r, c값이 없으면 바로 N*N값을 더해준다.(시간 초과 방지)
    if not(x <= r < x+N and y <= c < y+N):
        cnt += N*N
        return

    # 열부터 그리고 행부터 다시 분할재귀로 나눠 깊이로 들어간다.
    for k in range(2):
        for l in range(2):
            z(x+N//2*k, y+N//2*l, N//2)

z(0, 0, 2**N)