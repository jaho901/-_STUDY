import sys
sys.stdin = open('1713.txt')
from collections import defaultdict

n = int(input())
m = int(input())
num = list(map(int, input().split()))

rec = defaultdict()
for i in range(m) :
    if num[i] in rec.keys():
        rec[num[i]][0] += 1
    else :
        if len(rec) < n:
            rec[num[i]] = [1, i]
        else :
            # 횟수가 적으면서 가장 오래된 것 하나 제외
            del_key = sorted(rec.items(), key= lambda x :(x[1][0] , x[1][1]))[0][0]
            del(rec[del_key])
            rec[num[i]] = [1, i]

result = list(sorted(rec.keys()))
result = map(str, result)
print(' '.join(result))

