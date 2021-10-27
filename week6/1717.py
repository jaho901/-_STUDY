import sys
sys.stdin = open('1717.txt')

n, m = map(int, input().split())
parent = list(range(n+1))
rank = [0] * (n+1)

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    a = find(x)
    b = find(y)
    parent[b] = a

    '''
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1
    '''


for _ in range(m):
    a, u, v = map(int, input().split())
    if a == 0:
        union(u, v)
    elif a == 1:
        if find(u) == find(v):
            print('YES')
        else:
            print('NO')
        # print(parent)

