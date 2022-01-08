import sys
sys.stdin = open('1978.txt')

n = int(input())
data = list(map(int, input().split()))
result = 0

def find(num):
    if num == 1:
        cnt = 1
        return cnt

    cnt = 0
    for i in range(2, num):
        if i * i > num:
            break

        if num % i == 0:
            cnt += 1
    return cnt

for m in data:
    number = find(m)
    if number == 0:
        result += 1

print(result)