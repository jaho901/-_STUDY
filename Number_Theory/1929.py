import sys
sys.stdin = open('1929.txt')

n, m = map(int, input().split())

is_prime = [True] * (m + 1)

is_prime[1] = False
for i in range(2, m + 1):
    if i * i > m:
        break

    if not is_prime[i]:
        continue

    for j in range(i*i, m + 1, i):
        is_prime[j] = False

result = []
for i in range(n, m + 1):
    if is_prime[i]:
        result.append(i)

result = sorted(result)
for i in result:
    print(i)