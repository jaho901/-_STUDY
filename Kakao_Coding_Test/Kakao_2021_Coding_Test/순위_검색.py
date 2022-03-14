
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

'''
defaultdict()는 딕셔너리를 만드는 dict클래스의 서브클래스이다.

작동하는 방식은 거의 동일한데, defaultdict()는 인자로 주어진 객체(default-factory)의 기본값을 딕셔너리값의 초깃값으로 지정할 수 있다.

숫자, 리스트, 셋등으로 초기화 할 수 있기때문에 여러 용도로 사용할 수 있다.
'''

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    dic = defaultdict(list)
    result = []
    for i in info:
        i = i.split()
        other = i[:-1]
        score = int(i[-1])
        for i in range(len(info)):
            comb = list(combinations([0, 1, 2, 3], i))
            for c in comb:
                sub = other[:]
                for j in c:
                    sub[j] = "-"
                key = ''.join(sub)
                dic[key].append(score)

    for value in dic.values():
        value.sort()

    for qu in query:
        qu = qu.replace("and", "")
        qu = qu.split()
        target_key = "".join(qu[:-1])
        target_score = int(qu[-1])
        cnt = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            cnt = len(target_list) - idx
        result.append(cnt)
    return result

print(solution(info, query))


# def solution(info, query):
#     start = []
#     end = []
#     for i in info:
#         start.append(i.split())
#     for i in query:
#         sub = i.split()
#         sub_list = []
#         for j in sub:
#             if j != 'and':
#                 sub_list.append(j)
#         end.append(sub_list)
#     print(start)
#     print(end)
#     result = []
#
#     for i in end:
#         sub = 0
#         for k in start:
#             ans = 0
#             for j in range(len(i)):
#                 if j < len(i)-1 and (k[j] == i[j] or i[j] == '-'):
#                     ans += 1
#                 elif j == len(i)-1 and int(k[j]) >= int(i[j]):
#                     ans += 1
#                 else:
#                     break
#             if ans == len(i):
#                 sub += 1
#         result.append(sub)
#
#     return result
#
# print(solution(info, query))