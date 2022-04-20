import sys
sys.stdin = open('2531.txt')

n, d, k, c = map(int, input().split())
dishes = []
for i in range(n):
    dishes.append(int(input()))

result = 0

for i in range(n):
    sub = []
    for j in range(k):
        if i+j >= n:
            sub.append(dishes[(i+j)%n])
        else:
            sub.append(dishes[i+j])
    sub = set(sub)
    if c not in sub:
        sub.add(c)
    result = max(result, len(sub))

print(result)