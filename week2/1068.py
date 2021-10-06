import sys
sys.stdin = open('1068.txt')

N = int(input())
data = list(map(int, input().split()))
remover = int(input())
parent = data.index(-1)
data[remover] = -1
node = []

# 부모노드 제외하고 remover 포함한 자식노드 전부 -1로 변경
def remove(data):
    for i in range(remover, len(data)):
        if data[data[i]] == -1 and data[i] != parent:
            data[i] = -1
    return data


def dfs(parent):
    global ans
    # 만약에 부모노드에서의 자식노드가 존재하면
    if node[parent]:
        # 그 값들을 순서대로 dfs실시
        for i in node[parent]:
            dfs(i)
    # 만약에 자식노드가 없으면 ans에 1 더해주고
    # 다음번째의 i로 이동
    else:
        ans += 1



data = remove(data)
print(data)
# 존재하는 노드들의 연결리스트 생성
for i in range(N):
    sub = []
    for j in range(N):
        if data[j] == i:
            sub.append(j)
    node.append(sub)
print(node)
ans = 0
# 부모노드와 remover가 같으면 어차피 결과는 0
if parent == remover:
    print(ans)
# 그 외의 경우는 dfs 돌려서 나온 결과값 출력
else:
    dfs(parent)
    print(ans)
