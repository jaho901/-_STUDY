import sys
sys.stdin = open('11047.txt')

N, K = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

# 최종 결과값
result = 0
# 가장 큰 돈의 단위부터 작은 돈의 단위로 반복문 실행
for i in range(len(money)-1, -1, -1):
    # K원이 돈의 단위보다 작은경우 무시하고 넘어감
    if money[i] > K:
        continue
    # K원이 0이 되는 시점에 반복문 종료
    if K == 0:
        break
    # 결과값에 K원에서 해당하는 돈의 단위를 나눈 몫을 더해준다.
    result += K // money[i]
    # K원은 계속해서 나눠준 돈을 뺀 값으로 변경해준다.
    K = K % money[i]
print(result)