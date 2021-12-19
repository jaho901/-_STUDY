import sys
sys.stdin = open('14889.txt')
from itertools import combinations

'''
i,j 와 k,l의 차이의 최솟값 확인
N = 4면 3c2 = 3*2/2 = 3
1,2 - 3,4
1,3 - 2,4
1,4 - 2,3
N = 6면 5c3 = 5*4*3/3*2 = 10
1,2,3 - 4,5,6
1,2,4 - 3,5,6
1,2,5 - 3,4,6
1,2,6 - 3,4,5
1,3,4 - 2,5,6
1,3,5 - 2,4,6
1,3,6 - 2,4,5
3+6+8(17) - 5+8+6(19) 
1,4,5 - 2,3,6
1,4,6 - 2,3,5
1,5,6 - 2,3,4
'''

N = int(input())
soccer = [list(map(int, input().split())) for _ in range(N)]
n = int(N/2)
A = list(range(N))
comb = list(combinations(A, n))
length = len(comb)//2
data = []
for i in range(length):
    data.append([comb[i], comb[-(i+1)]])
result = 100000000

for i in data:
    a, b = 0, 0
    comb_1 = list(combinations(i[0], 2))
    comb_2 = list(combinations(i[1], 2))
    for j in comb_1:
        a += (soccer[j[0]][j[1]] + soccer[j[1]][j[0]])
    for k in comb_2:
        b += (soccer[k[0]][k[1]] + soccer[k[1]][k[0]])
    diff = abs(a-b)
    if result > diff:
        result = diff

print(result)

