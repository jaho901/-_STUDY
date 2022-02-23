fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

# fees = [1, 461, 1, 10]
# records = ["00:00 1234 IN"]

# fees = [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
# records 에서 (OUT으로 된거 시각 - IN으로 된거 시각) if 180이상 =>

def solution(fees, records):
    result = dict()
    sub = []
    # 차별 시간 총합 저장본
    answer = []

    # 차량 번호 순서대로 딕셔너리 정렬
    for i in range(len(records)):
        timein, number, type = records[i].split()
        if number not in result:
            result[number] = 0
    result = sorted(result.items())
    result = dict(result)
    # print(result)

    # 시간을 각각의 번호에 맞게 추가
    for i in range(len(records)):
        timein, number, type = records[i].split()
        if type == 'IN':
            sub.append([timein, number])

        elif type == 'OUT':
            for j in range(len(sub)):
                ti, num = sub[j][0], sub[j][1]
                if num == number:
                    numberout = num
                    timeout = ti
                    sub.pop(j)
                    break
            time = (int(timein[:2])*60+int(timein[3:]) - (int(timeout[:2])*60+int(timeout[3:])))
            result[numberout] += time
    # print(result)
    for x, y in sub:
        result[y] += ((23*60+59)-(int(x[:2])*60+int(x[3:])))
    # print(result)
    basic_time, basic_fee, per_time, per_fee = fees[0], fees[1], fees[2], fees[3]

    for i, key in enumerate(result):
        if result[key] <= basic_time:
            answer.append(basic_fee)
        else:
            if (result[key] - basic_time)%per_time==0:
                answer.append(basic_fee + ((result[key] - basic_time)//per_time)*per_fee)
            else:
                answer.append(basic_fee + (((result[key] - basic_time) // per_time)+1) * per_fee)

    return answer



print(solution(fees, records))