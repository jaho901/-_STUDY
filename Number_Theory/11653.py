import sys
sys.stdin = open('11653.txt')

n = int(input())

x = n
for i in range(2, n + 1):
    if i * i > n: # 루트 n보다 크거나 같은 소인수는 최대 1개 존재!
        break

    while x % i == 0:
        print(i)
        x //= i

if x != 1:
    print(x)