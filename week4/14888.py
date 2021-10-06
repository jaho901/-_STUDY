import sys
sys.stdin = open('14888.txt')

N = int(input())
number = list(map(int, input().split()))
# operator = ['+', '-', '*', '/']
plus, minus, product, div = map(int, input().split())
M = plus + minus + product + div
# M = N-1
def dfs(cur, total):
    global ans_min, ans_max, plus, minus, product, div

    # 마지막 깊이까지 들어가게 된다면 max값과 min값을 따로 구해서 리턴
    if cur == M+1:
        ans_max = max(ans_max, total)
        ans_min = min(ans_min, total)
        return

    # 각각의 연산자에 맞게 나눠서 재귀들어가준다. ( 조합이기 때문에 마지막에 다시 1씩 더해준다. )
    if plus > 0:
        plus -= 1
        dfs(cur+1, total+number[cur])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(cur+1, total-number[cur])
        minus += 1
    if product > 0:
        product -= 1
        dfs(cur+1, total*number[cur])
        product += 1
    if div > 0:
        div -= 1
        dfs(cur+1, int(total/number[cur]))
        div += 1

ans_min = 100000000
ans_max = -100000000
dfs(1, number[0])
print(ans_max)
print(ans_min)