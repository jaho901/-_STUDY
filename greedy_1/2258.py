import sys
sys.stdin = open('2258.txt')

N, M = map(int, input().split())
data = []
# 데이터에 가격, 무게 순으로 넣어주고
# 그 값을 가격은 오름차순, 무게는 내림차순으로 넣어준다.
# why? => 같은 가격에서 무게가 많이 나가는 고기를 얻기 위해!!
for _ in range(N):
    w, p = map(int, input().split())
    data.append([p, w])
data = sorted(data, key=lambda x : [x[0], -x[1]])
print(data)
weight = data[0][1]
# 아래값보다 더 큰 값을 넣어주면 틀림
# 문제가 약간 찌질한 수준...
result = 2147483647
# 같은 가격인 경우 same값에 저장!!
same = 0
# 불가능한 경우를 확인하기 위해 생성
exist = False

# 범위는 그 전값을 제외해서 1부터 지정
for i in range(1, len(data)):
    weight += data[i][1]
    # 동일한 가격일 경우 그 가격을 same에 저장
    if data[i][0] == data[i-1][0]:
        same += data[i-1][0]
    # 아닐경우 same 초기화
    else:
        same = 0

    # 우리가 원하는 값 M을 넘을 경우
    if weight >= M:
        # 계속해서 result값과 현재 가격에 same을 더해준 값을 비교해서
        # 더 작은 값을 result에 저장시킨다.
        result = min(result, data[i][0] + same)
        exist = True

# True이면 새로운 result값이 있으니 result값 도출
if exist:
    print(result)
# 그 외에는 불가능한 경우이니 -1 도출
else:
    print(-1)

