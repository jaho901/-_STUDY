import sys
sys.stdin = open('2668.txt')
# from itertools import combinations
# from collections import defaultdict
#
# n = int(input())
# data = defaultdict()
# for i in range(1, n+1):
#     data[i] = int(input())
#
# comb = []
# for i in range(1, n+1):
#     comb += list(combinations(data, i))
#
# result = []
# for i in comb:
#     sub = []
#     for j in range(len(i)):
#         sub.append(data[i[j]])
#     if sorted(list(i)) == sorted(sub) and len(sub) >= len(result):
#         result = sub
# result = sorted(result)
# print(len(result))
# for i in result:
#     print(i)

'''
여기서 우리가 알아야 할 점은
idx => data[idx]인 경우
1. idx == data[idx]이면 바로 result에 추가
2. data[data[idx]] => idx이면 바로 result에 추가
'''

def dfs(v, i):
    visited[v] = True

    for w in data[v]:
        if not(visited[w]):
            dfs(w, i)
        elif visited[w] and w == i:
            result.append(w)

T = int(input())
data = [[] for i in range(T+1)]
for i in range(T):
    data[i+1].append(int(input()))
result = []
for i in range(1, T+1):
    visited = [False] * (T + 1)
    dfs(i, i)
l = len(result)
print(l)
for i in range(l):
    print(result[i])