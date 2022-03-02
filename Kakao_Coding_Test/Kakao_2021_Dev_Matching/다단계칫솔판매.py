enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

# enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# seller = ["sam", "emily", "jaimie", "edward"]
# amount = [2, 3, 5, 4]

result = []

def solution(enroll, referral, seller, amount):
    global result
    result = [0 for _ in range(len(enroll))]

    def dfs(start, next, value):
        global result
        if next == "-":
            final_idx = enroll.index(start)
            result[final_idx] += value - value // 10
            return
        s_idx = enroll.index(start)
        e_idx = enroll.index(next)
        if value * 0.1 > 1:
            result[s_idx] += value - value // 10
            new_value = value // 10
        else:
            new_value = 0
        new_next = referral[e_idx]
        dfs(next, new_next, new_value)

    for i in range(len(amount)):
        idx = enroll.index(seller[i])
        value = amount[i]*100
        dfs(seller[i], referral[idx], value)
    return result


print(solution(enroll, referral, seller, amount))

