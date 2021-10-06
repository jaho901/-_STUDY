import sys
sys.stdin = open('1780.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

num_0 = 0
num_1 = 0
num_minus = 0

def find(x, y, N):
    global num_0, num_1, num_minus
    # 가장 처음에 위치한 값을 first로 저장
    first = arr[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            # 만약에 first와 같은 값이 존재하지 않는다면
            if arr[i][j] != first:
                # 3/1씩 나눠서 분할 재귀 실행
                for k in range(3):
                    for l in range(3):
                        find(x + N//3*k, y + N//3*l, N//3)
                return
    
    if first == 0:
        num_0 += 1
    elif first == 1:
        num_1 += 1
    else:
        num_minus += 1


find(0, 0, N)
print(num_minus)
print(num_0)
print(num_1)

