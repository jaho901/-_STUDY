import sys
sys.stdin = open('1439.txt')

num = list(map(int,input()))
# 0과 1을 1개씩 줄여서 넣을 리스트
result = []
for i in range(len(num)-1):
    # 중복되면 무시
    if num[i] == num[i+1]:
        continue
    # 중복되지 않으면 result에 추가
    else:
        result.append(num[i])
# 마지막 값은 무조건 append!
result.append(num[-1])
a = result.count(0)
b = result.count(1)
# 0의 개수와 1의 개수중 작은 값 도출
if a < b:
    print(a)
elif a > b:
    print(b)
else:
    print(a)