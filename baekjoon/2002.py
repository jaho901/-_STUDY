import sys
sys.stdin = open('2002.txt')

N = int(input())
start = []
end = []
for i in range(N*2):
    if i < N:
        start.append(input())
    else:
        end.append(input())

result = 0
cnt = 0
i = 0
while True:
    end_idx = i
    start_idx = start.index(end[i])
    end.pop(end_idx)
    start.pop(start_idx)
    if end_idx < start_idx:
        result += 1
    cnt += 1
    if cnt == N:
        break

print(result)