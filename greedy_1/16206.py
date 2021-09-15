
T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    cake = []
    sub = []
    result = 0
    for i in range(len(data)):
        # 롤 케잌이 10이면 자를 필요가 없기 때문에 그 개수만큼 result에 추가하고 값은 넣지말자!
        if data[i] == 10:
            result += 1
        # 10이 아니면서 10의 배수인값들을 cake리스트에 넣기
        elif data[i] != 10 and data[i]%10 == 0:
            cake.append(data[i])
        # 10의 배수가 아닌 값들을 sub리스트에 넣기
        else:
            sub.append(data[i])
    # cake리스트가 우선으로 온 뒤에 sub리스트 더하기
    cake = sorted(cake) + sub
    # print(cake)
    # cake 리스트가 존재할 경우
    if cake:
        for j in range(len(cake)):
            # 10의 배수인 경우
            if cake[j]%10==0:
                # 그 몫을 k로 저장
                k = cake[j] // 10
                # k가 (자를 수 있는 횟수 + 1)보다 작거나 같은경우
                # ex) 롤케잌 = 20, 자를 수 있는 기회 = 1 이 경우 롤케잌을 잘라서 2개의 결과값을 얻을 수 있기 때문에!!
                if k <= M+1:
                    # 그 값만큼 result와 M을 변경해준다.
                    result += k
                    M -= k-1
                # 만약에 케잌이 자를 수 있는 기회보다 더 길 경우
                else:
                    # 자른 만큼만 result에 더해주고 반복문 종료!
                    result += M
                    break
            # 10의 배수가 아닌 경우
            else:
                # 자른 횟수만큼의 값만 result에 추가해주고 M을 변경해준다.
                k = cake[j] // 10
                if k <= M:
                    result += k
                    M -= k
                else:
                    result += M
                    break
            # M이 음수가 아닌 딱 0인 경우도 멈춰준다.
            if M == 0:
                break
        print(result)
    else:
        print(result)






'''
# 완탐으로 풀기!!!
T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    cake = []
    sub = []
    result = 0
    for i in range(len(data)):
        if data[i] == 10:
            result += 1
        elif data[i] != 10 and data[i]%10 == 0:
            cake.append(data[i])
        else:
            sub.append(data[i])
    cake = sorted(cake) + sub

    if cake:
        while M > 0:
            for i in range(len(cake)):
                while cake[i] > 10:
                    cake[i] -= 10
                    M -= 1
                    result += 1
                    if cake[i] == 10:
                        result += 1
                        break
                    if M == 0:
                        break
                if M == 0:
                    break
        print(result)
    else:
        print(result)
'''