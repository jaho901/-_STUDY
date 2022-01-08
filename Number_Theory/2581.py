import sys
sys.stdin = open('2581.txt')

n = int(input())
m = int(input())

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

print(result)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(result[0])