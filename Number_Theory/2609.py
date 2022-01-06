import sys
sys.stdin = open('2609.txt')

n, m = map(int, input().split())
N, M = n, m
# GCD
while M != 0:
    N, M = M, N%M

print(N)

# LCM
N, M = n, m
# 유클리드 호제법
while N % M != 0:
    N, M = M, N%M

print(n * m // M)