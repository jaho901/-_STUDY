import sys
sys.stdin = open('2668.txt')
from itertools import combinations
from collections import defaultdict

n = int(input())
data = defaultdict()
for i in range(1, n+1):
    data[i] = int(input())

comb = []
for i in range(1, n+1):
    comb += list(combinations(data, i))

result = []
for i in comb:
    sub = []
    for j in range(len(i)):
        sub.append(data[i[j]])
    if sorted(list(i)) == sorted(sub) and len(sub) >= len(result):
        result = sub
result = sorted(result)
print(len(result))
for i in result:
    print(i)