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

'''
def solution(enroll, referral, seller, amount):
    dic = dict(zip(enroll, referral))           # {사람: 추천인} 구조
    ans = dict(zip(enroll, [0]*len(enroll)))    # {사람: 이익} 구조

    for i in range(len(seller)):
        person = seller[i]
        price = amount[i] * 100         # 칫솔 개당 100원
        while True:
            ans[person] += price        # 판매
            if price < 10: break        # 추천인에게 줄 거 없음
            ten = int(price*0.1)        # 10% 계산
            ans[person] -= ten          # 10% 삭감
            person = dic[person]        # 추천인은 누구?
            if person == '-': break     # 추천없이 참여했으면 stop
            price = ten                 # 추천인이 있으면 가격 갱신하고 while
    return list(ans.values())
'''