import sys
sys.stdin = open('3671.txt')

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True

def make_int(str_list):
    ans = ''
    for i in str_list:
        ans += i
    ans = int(ans)
    return ans

def permutation(cur, i):
    global perm

    if cur == i:
        if is_prime(make_int(sub)):
            perm.add(make_int(sub))
        return

    for k in range(len(n)):
        if visited[k]:
            continue

        visited[k] = True
        sub.append(n[k])
        permutation(cur+1, i)
        sub.pop()
        visited[k] = False

t = int(input())
for _ in range(t):
    n = input()
    n = list(n)
    perm = set()
    for i in range(1, len(n)+1):
        visited = [False] * len(n)
        sub = []
        permutation(0, i)
    perm = set(perm)
    print(len(perm))

