# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]


def solution(lottos, win_nums):
    lottos = sorted(lottos)
    zero_num = 0
    right_num = 0

    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_num += 1
        else:
            if lottos[i] in win_nums:
                right_num += 1

    if right_num <= 1:
        min_num = 6
    else:
        min_num = 7-right_num
    if right_num+zero_num <= 1:
        max_num = 6
    else:
        max_num = 7-(right_num+zero_num)
    result = [max_num, min_num]
    return result

print(solution(lottos, win_nums))