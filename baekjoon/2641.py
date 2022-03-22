import sys
sys.stdin = open('2641.txt')
from copy import deepcopy
from collections import deque

# 1 : 오른쪽 / 2 : 위쪽 / 3 : 왼쪽 / 4 : 아래쪽

length = int(input())
example = list(map(int, input().split()))
example_pop = deepcopy(example)
n = int(input())
example_list = [list(map(int, input().split())) for _ in range(n)]

sample = []
while example_pop:
    sub = example_pop.pop()
    if sub == 1:
        sample.append(3)
    elif sub == 2:
        sample.append(4)
    elif sub == 3:
        sample.append(1)
    elif sub == 4:
        sample.append(2)

example = deque(example)
sample = deque(sample)
result = []

for i in example_list:
    for j in range(length):
        if i == list(example):
            result.append(i)
        if i == list(sample):
            result.append(i)
        example.rotate(-1)
        sample.rotate(-1)

print(len(result))
for k in result:
    print(*k)