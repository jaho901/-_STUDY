import sys
sys.stdin = open('14465.txt')

N, K, B = map(int, input().split())
bp = []
# 이동 불가능한 위치 전부 bp에 저장
for _ in range(B):
    bp.append(int(input()))

result = 100000
'''
여기서 내가 생각한 로직
=> 1~K, 2~K+1, ... , N-K+1~N
   의 범위에 존재하는 bp의 개수가 가장 적은 경우에 bp의 개수가 정답
'''
s, e = 1, K
while True:
    sub = 0
    # 각각의 범위에 존재하는 bp의 개수 확인하여 sub에 저장
    for p in bp:
        if s <= p <= e:
            sub += 1

    result = min(result, sub)
    s += 1
    e += 1
    # 마지막 범위에 도착하면 종료
    if e == N+1:
        break

print(result)