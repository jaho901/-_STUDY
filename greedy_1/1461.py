import sys
sys.stdin = open('1461.txt')

# 가장 큰 값부터(음수 -> 양수) K개씩의 시작값을 넣는 함수
def cal(data):
    result = []
    for i in range(0, len(data), K):
        result.append(abs(data[i]))
    return result

N, K = map(int, input().split())
location = list(map(int, input().split()))
# 음수값
ne_lo = []
# 양수값
po_lo = []
for i in location:
    if i < 0:
        ne_lo.append(i)
    else:
        po_lo.append(i)
# 음수값과 양수값을 모두 절대값이 큰 값부터 작은값으로 정렬
ne_lo = sorted(ne_lo)
po_lo = sorted(po_lo, reverse=True)
# print(ne_lo, po_lo)
total = []

# 음수에서 cal함수 사용해서 더해주고
# 양수에서 cal함수 사용해서 더해준다.
# K==2일때, 어차피 음수1개, 양수1개라도 그 값만큼 왕복으로 이동해야하기 때문에 6과 11이 total에 더해진것이다.
total += cal(ne_lo)
total += cal(po_lo)
total = sorted(total)
ans = 0
# 가장 큰 값은 맨 마지막에 옮기면서 왕복의 필요가 없어진다.
# 즉, 그 값만 더해준다.
ans += total.pop()
# 그 외의 값들은 2를 곱한 값으로 (왕복) 더해준다.
ans += sum(total)*2
print(ans)
