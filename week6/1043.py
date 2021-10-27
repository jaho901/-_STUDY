import sys
sys.stdin = open('1043.txt')

n, m = map(int, input().split())
parent = list(range(n+1))
true_people = list(map(int, input().split()))

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


if true_people[0] == 0:
    print(m)

else:
    true_num = true_people[0]
    true_people = true_people[1:]
    # 진실을 아는 자들 한 그룸으로 만들기
    for i in range(true_num):
        union(true_people[0], true_people[i])

    groups = []

    for _ in range(m):
        groups.append(list(map(int, input().split())))
        num = groups[-1][0]
        # 1개만 존재하면 무시
        # 2개이상존재할때만 존재하는 것들끼리 합집합!!
        for i in range(num-1):
            union(groups[-1][i+1], groups[-1][i+2])

    result = 0
    for group in groups:
        if find(group[1]) == find(true_people[0]):
            result += 1
    print(m-result)

