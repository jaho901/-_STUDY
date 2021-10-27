import sys
sys.stdin = open('10775.txt')

G = int(input())
P = int(input())
air = []
for _ in range(P):
    air.append(int(input()))

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    parent[b] = a


parent = list(range(G+1))
result = 0

for i in air:
    x = find(i)
    if x == 0:
        break
    union(x-1, x)
    result += 1

print(result)