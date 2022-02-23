id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

def solution(id_list, report, k):
    n = len(id_list)
    report_list = [[] for _ in range(n)]
    stop_list = [0] * n
    stop = []
    report = list(set(report))

    for i in report:
        user, report_user = i.split()
        user_idx = id_list.index(user)
        report_idx = id_list.index(report_user)
        report_list[user_idx].append(report_idx)
    print(report_list)
    for i in range(len(report_list)):
        for j in report_list[i]:
            stop_list[j] += 1
    print(stop_list)
    for i in range(len(stop_list)):
        if stop_list[i] >= k:
            stop.append(i)
    print(stop)
    result = [0] * n

    for i in range(len(report_list)):
        for j in report_list[i]:
            if j in stop:
                result[i] += 1

    return result


print(solution(id_list, report, k))