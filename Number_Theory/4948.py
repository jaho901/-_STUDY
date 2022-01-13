import sys
sys.stdin = open('4948.txt')

while True:
    n = int(input())
    if n == 0:
        break

    is_prime = [True] * (2*n + 1)
    is_prime[1] = False

    for i in range(2, 2*n + 1):
        if i * i > 2*n:
            break

        if not is_prime[i]:
            continue

        for j in range(i * i, 2*n + 1, i):
            is_prime[j] = False

    cnt = 0
    for i in range(n+1, 2*n + 1):
        if is_prime[i]:
            cnt += 1

    print(cnt)

