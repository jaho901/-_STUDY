import sys
sys.stdin = open('2981.txt')

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
data = sorted(data, reverse=True)

diff = []
for i in range(len(data)-1):
    diff.append(data[i] - data[i+1])

# 약수
def aliquot(n):
    aliquot_list = []
    for i in range(1, n + 1):
        if i * i > n:
            break

        if n % i == 0:
            aliquot_list.append(i)
            if i * i != n:
                aliquot_list.append(n // i)
    return aliquot_list

# 최대공약수
def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

if len(diff) == 1:
    result = diff[0]
elif len(diff) == 2:
    result = gcd(diff[0], diff[1])
else:
    result = diff[0]
    for i in range(1, len(diff)):
        result = gcd(result, diff[i])

# 나온 result의 모든 약수 구하기
result = sorted(aliquot(result))
result = result[1:]
print(*result)