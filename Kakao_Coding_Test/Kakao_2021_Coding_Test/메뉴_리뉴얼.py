# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

from itertools import combinations

def solution(orders, course):
    result = []
    for num in course:
        sub_list = []
        menus = {}
        for menu in orders:
            for i in combinations(list(''.join(menu)), num):
                sub = ''.join(sorted(i))
                # 없으면 추가
                if sub not in sub_list:
                    sub_list.append(sub)
                # 있으면 변경
                else:
                    # sub_list에는 있고 menus에는 없으면 menus에 그 전꺼+이번꺼로 2로 변경
                    if sub not in menus.keys():
                        menus[sub] = 2
                    # 전부 해당안되면 += 1씩
                    else:
                        menus[sub] += 1
        menus = sorted(menus.items(), key=lambda x:[-x[1], x[0]])
        if menus:
            sub = menus[0][1]
            result.append(menus[0][0])
            for i in range(1, len(menus)):
                if menus[i][1] == sub:
                    result.append(menus[i][0])
                else:
                    break
    result = sorted(result)
    return result


print(solution(orders, course))