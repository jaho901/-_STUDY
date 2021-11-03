import sys
sys.stdin = open('1043.txt')

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

# n, m 받아오며 부모노드리스트 생성
n, m = map(int, input().split())
parent = list(range(n+1))
# 진실을 아는 사람의 수를 받아온다.
true_people = list(map(int, input().split()))

# 진실을 아는 사람이 0이면 모든 파티에서 과장된 얘기를 할 수 있다.
if true_people[0] == 0:
    print(m)

else:
    # 가장 앞 번호는 진실을 아는 인원수 == true_num
    true_num = true_people[0]
    # 그 이후는 진실을 아는 사람의 번호 == true_people
    true_people = true_people[1:]
    # 진실을 아는 자들 한 그룸으로 만들기
    for i in range(true_num):
        union(true_people[0], true_people[i])

    # 각각의 파티 정보 담을 리스트
    groups = []

    for _ in range(m):
        groups.append(list(map(int, input().split())))
        num = groups[-1][0]
        # 1개만 존재하면 무시
        # 2개이상존재할때만 존재하는 것들끼리 합집합!!
        for i in range(num-1):
            union(groups[-1][i+1], groups[-1][i+2])

    result = 0
    # 각각의 그룹들을 확인하면서 그 그룹의 부모가 진실을 알고있으면 1씩 추가
    for group in groups:
        if find(group[1]) == find(true_people[0]):
            result += 1
    # 총 인원에서 result값 빼주기
    print(m-result)

