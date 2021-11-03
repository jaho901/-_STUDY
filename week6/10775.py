import sys
sys.stdin = open('10775.txt')

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


G = int(input())
P = int(input())
air = []
for _ in range(P):
    air.append(int(input()))

parent = list(range(G+1))
result = 0

# 여기서 중요한거는 비행기는 gi번째부터 아래로 찾아가며 도킹해야한다.
'''
223344 순이면
처음 -> [0, 1, 2, 3, 4]
2 -> [0, 1, 1, 3, 4]
2 -> [0, 0, 0, 3, 4]
3 -> [0, 0, 0, 0, 4]
3 -> x = 0 => break
'''
for i in air:
    # x는 부모노드
    x = find(i)
    if x == 0:
        break
    # x가 x-1에 포함되게 합집합 생성
    union(x-1, x)
    result += 1

print(result)