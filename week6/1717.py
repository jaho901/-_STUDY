import sys
sys.stdin = open('1717.txt')

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
    # union by rank
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[a] = b
        rank[b] += 1
    '''

# n, m을 받아온다.
n, m = map(int, input().split())
# 부모노드를 저장할 parent 리스트 생성
parent = list(range(n+1))
# union by rank를 위한 리스트 생성
rank = [0] * (n+1)

for _ in range(m):
    # t = 0 or 1 | a, b 받아옴
    t, a, b = map(int, input().split())
    # t가 0이면 합집합을 만들기 위해 union함수 사용
    if t == 0:
        union(a, b)
    # t가 1이면 a와 b가 같은 집합에 있는지를 확인
    elif t == 1:
        # 만약 a와 b의 부모노드가 동일하면 같은 집합이니 'YES' 반환
        if find(a) == find(b):
            print('YES')
        # 부모노드가 다르면 다른 집합이니 'NO' 반환
        else:
            print('NO')
        # print(parent)

