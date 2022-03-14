'''
1번

3개의 숫자 mod1, mod2, max_range가 주어집니다.
1 이상 max_range 이하의 자연수 중에서 mod1로 나누어떨어지지만,
mod2로 나누어떨어지지 않는 수의 개수를 return 하도록 solution 함수를 완성하세요.

mod1 = 4
mod2 = 3
max_range = 20
# mod1 = 3
# mod2 = 4
# max_range = 20

def solution(mod1, mod2, max_range):
    mod1_cnt = max_range//mod1
    A, B = mod1, mod2
    while A % B != 0:
        A, B = B, A % B

    lcm = mod1 * mod2 // B

    both_cnt = max_range//lcm
    result = mod1_cnt-both_cnt

    return result

print(solution(mod1, mod2, max_range))
'''

'''
2번

로봇이 이동할 수 있는 레일이 설치된 도로가 있습니다. 
도로는 일정 크기의 블록으로 나뉘어 있으며, 각 블록에는 '>' 또는 '<' 기호가 표시되어있습니다. 
로봇은 블록에 표시된 기호를 인식하여 이동합니다. 
만약 '>'가 표시되어있다면 로봇은 1칸 오른쪽으로, '<'가 표시되어있다면 로봇은 1칸 왼쪽으로 이동합니다. 
로봇은 도로의 아무 블록에서나 출발할 수 있으며, 로봇의 최종 목표는 도로를 빠져나오는 것입니다. 
이때, 로봇이 도로를 빠져나올 수 있는 출발점의 개수를 구하는 것이 목표입니다.

예를 들어, 도로가 <<<>< 라면, 1번째 블록, 2번째 블록, 3번째 블록에 로봇을 두면 왼쪽 밖으로 빠져나올 수 있지만, 
4번째 블록과 5번째 블록에 로봇을 두면 어느 방향으로도 밖으로 빠져나올 수 없으므로 
빠져나올 수 있는 출발점은 1번째 블록, 2번째 블록, 3번째 블록이므로 출발점의 개수는 3개가 됩니다. 
도로의 블록에 표시된 기호가 문자열 P로 주어질 때, 도로를 빠져나올 수 있는 출발점의 개수를 return 하는 solution 함수를 완성해 주세요.

p = "<<<><"

# 결국 왼쪽부터 "<"의 개수와 오른쪽부터 ">"의 개수를 구하는거 아닌가?

def solution(p):
    result = 0
    for i in range(len(p)):
        if p[i] == "<":
            result += 1
        else:
            break
    for j in range(len(p)-1, -1, -1):
        if p[j] == ">":
            result += 1
        else:
            break
    return result

print(solution(p))
'''

'''
3번

보험 항목별 보장 금액이 순서대로 들어있는 배열이 있습니다. 
주어진 항목 중에서 k개 이상의 항목을 선택하여 새 보험 상품을 만들되, 새 보험 상품에 포함되는 각 항목의 보장 금액의 
합이 t 이하가 되도록 하려고 합니다. 다음은 항목별 보장 금액이 들어있는 배열 [2, 5, 3, 8, 1], k = 3, t = 11 이 주어진 경우의 예시입니다.
먼저 주어진 배열은 5개의 보험 항목의 보장 금액이 순서대로 [2, 5, 3, 8, 1]임을 나타냅니다. 
이때, 3개 이상의 항목을 선택하는 방법은 총 16가지가 있는데, 이 중, 선택된 항목들의 보장 금액의 합이 11 이하가 되는 경우는 
다음과 같이 6가지가 있습니다.
[2, 5, 3]
[2, 5, 1]
[5, 3, 1]
[2, 3, 1]
[2, 8, 1]
[2, 5, 3, 1]
예를 들어 선택한 항목의 보장 금액이 [2, 5, 3, 1] 인 경우 보장 금액의 합은 2 + 5 + 3 + 1 = 11이므로 11 이하가 됩니다. 
그러나 만약 선택한 항목의 보장 금액이 [5, 3, 8]인 경우 보장 금액의 합은 5 + 3 + 8 = 16이므로 이 경우는 불가능한 방법이 됩니다.
항목별 보장 금액이 순서대로 들어있는 배열 arr와 k, t가 매개변수로 주어질 때, arr에서 k개 이상의 항목을 선택했을 때, 
금액 합이 t 이하가 되도록 하는 경우의 수를 return 하도록 solution 함수를 완성해주세요.

arr = [2, 5, 3, 8, 1]
k = 3
t = 11
# arr = [1,1,2,2]
# k = 2
# t = 3
# arr = [1,2,3,2]
# k = 2
# t = 2
from itertools import combinations

def solution(arr, k, t):
    data = []
    for num in range(k, len(arr)+1):
        data += list(combinations(arr, num))
    result = 0
    for i in data:
        if sum(i) <= t:
            print(i)
            result += 1
    return result

print(solution(arr, k, t))

'''

'''
4번

게임에 접속한 모든 유저에게 아이템을 지급하는 출석 이벤트를 k일 동안 진행하려 합니다. 
날짜별 추정 접속자 수가 주어질 때, k일 동안 추정 접속자 수의 합이 최대가 되도록 이벤트 기간을 정하려 합니다.

날짜별 추정 접속자 수가 순서대로 담긴 배열 estimates와 출석 이벤트를 진행하는 기간 k가 매개변수로 주어집니다.
k일 동안 추정 접속자 수의 합이 최대가 되도록 이벤트 기간을 정했을 때, 그 때의 추정 접속자 수 합을 
return 하도록 solution 함수를 완성해주세요.

# estimates = [5,1,9,8,10,5]
# k = 3
estimates = [10,1,10,1,1,4,3,10]
k = 6

def solution(estimates, k):
    s, e = 0, k
    summation = sum(estimates[s:e])
    result = summation
    for i in range(k, len(estimates)):
        summation = summation - estimates[i-k] + estimates[i]
        result = max(result, summation)
    return result

print(solution(estimates, k))
'''

'''
5번
금 한 돈의 값은 매일 변합니다. 금값이 낮을 때 금을 사고, 높을 때 팔면 이익을 낼 수 있습니다. 
다음 규칙에 맞게 금을 사고팔아 이익을 남기려고 합니다.

금은 여러 번 사고팔 수 있습니다.
금을 살 때는 한 돈만 살 수 있으며 팔 때도 한 돈만 팔 수 있습니다.
금은 최대 한돈 까지만 가지고 있을 수 있습니다. (즉, 현재 가지고 있는 금을 팔기 전까지는 금을 살 수 없습니다.)
금을 판 날과 다음날에는 금을 사지 않습니다.
이익이 발생하지 않는다면 금을 사고팔지 않아도 됩니다.
i번째 요소가 i번째 일의 금 한 돈의 값인 배열 gold_prices가 매개변수로 주어질 때, 금을 사고팔아 얻을 수 있는 
최대 이윤을 return 하도록 solution 함수를 완성해 주세요.

'''

# gold_prices = [2,5,1,3,4]
gold_prices = [7,2,5,6,1,4,2,8]
result = 0

def dfs(cur, total, gold):
    global result, gold_list
    if cur >= len(gold_list):
        if total > result:
            result = total
        return


    for i in range(cur, len(gold_list)):
        if gold!=0 and gold < gold_list[i]:
            dfs(i+2, total + gold_list[i] - gold, 0)
        elif gold==0:
            dfs(i+1, total, gold_list[i])

def solution(gold_prices):
    global result, gold_list
    gold_list = gold_prices[:]
    dfs(0, 0, 0)
    return result

print(solution(gold_prices))





'''
6번
grid에서 K*K 장소를 2개 찾는데 겹치면 안되고 각 장소에 있는 숫자 합이 가장 큰 경우의 합을 구하라.


# grid = [[3, 4, 5], [2, 3, 4], [1, 2, 3]]
# K = 1
grid = [[2, 1, 1, 0, 1], [1, 2, 0, 3, 0], [0, 1, 5, 1, 2], [0, 0, 1, 3, 1], [1, 2, 0, 1, 1]]
K = 2

def solution(grid, K):
    result = 0
    num = len(grid)-K+1
    for i in range(num):
        for j in range(num):
            sum_a = 0
            for x in range(i, i+K):
                for y in range(j, j+K):
                    sum_a += grid[x][y]
            for k in range(num):
                if k < i+K:
                    for l in range(j+K, num):
                        sum_b = 0
                        for z in range(k, k+K):
                            for w in range(l, l+K):
                                sum_b += grid[z][w]
                        if result < sum_a + sum_b:
                            result = sum_a + sum_b
                else:
                    for l in range(num):
                        sum_b = 0
                        for z in range(k, k+K):
                            for w in range(l, l+K):
                                sum_b += grid[z][w]
                        if result < sum_a + sum_b:
                            result = sum_a + sum_b
    return result

print(solution(grid, K))

# 0,0 안되는거 0, K / K, 0 / K, K
from itertools import combinations
def solution(grid, K):
    case = []
    num = len(grid)-K+1
    for i in range(num):
        for j in range(num):
            case.append([i,j])
    data = list(combinations(case, 2))
    # 규칙
    # 1. b_x - a_x < K 불가능
    # 2. b_y - a_y < K 불가능
    # 3. b_x - a_x < K 이면서 b_y - a_y < K 불가능
    comb = []
    for i in data:
        a_x, a_y, b_x, b_y = i[0][0], i[0][1], i[1][0], i[1][1]
        if b_x - a_x >= K or b_y - a_y >= K:
            comb.append(i)
    print(comb)
    result = 0
    for i in comb:
        a_x, a_y, b_x, b_y = i[0][0], i[0][1], i[1][0], i[1][1]
        sum_a, sum_b = 0, 0
        for x in range(a_x, a_x+K):
            for y in range(a_y, a_y+K):
                sum_a += grid[x][y]
        for w in range(b_x, b_x+K):
            for z in range(b_y, b_y+K):
                sum_b += grid[w][z]
        result = max(result, sum_a+sum_b)

    return result

print(solution(grid, K))
'''






