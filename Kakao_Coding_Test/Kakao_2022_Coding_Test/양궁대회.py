
# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]

# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

# n = 10
# info = [0,0,0,0,0,0,0,0,3,4,3]


'''
어피치 n발 => 라이언 n발
1. 가장 안쪽부터 10 -> 9 -> ... -> 0
2. k점 어피치가 a발, 라이언이 b발 => 더 많이 맞춘 선수가 k점 가져감
    -> 여기서 a = b인 경우 먼저 쏜 어피치가 k점 가져감
3. 최종 점수가 더 높은 선수 == 우승자
    -> 최종 점수가 같을 경우 어피치가 승리
여기서 라이언이 어피치를 가장 큰 첨수 차이로 이기기 위한 n발의 화살 점수표!!
만약 라이언이 우승 못할 경우 [-1] return

info : 총합 = n / [10, 9, ... , 0] 의 점수를 맞춘 횟수
라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우,
가장 낮은 점수를 더 많이 맞힌 경우를 return
'''

result = []
total = 0
def solution(n, info):
    global result

    answer = [0] * 11

    def recur(cur, index):
        global result, total
        if cur == n:
            peach, lion = 0, 0
            for i in range(11):
                if info[i] >= answer[i] and info[i] != 0:
                    peach += (10-i)
                elif info[i] < answer[i] and answer[i] != 0:
                    lion += (10-i)
            if lion > peach:
                diff = lion - peach
                if diff > total:
                    result = [answer[:]]
                    total = diff
                elif diff == total:
                    result.append(answer[:])
            return

        for i in range(index, 11):
            answer[i] += 1
            recur(cur+1, i)
            answer[i] -= 1

    recur(0, 0)
    print(result)
    if result==[]:
        result = [-1]
    elif len(result) == 1:
        result = result[0]
    else:
        for i in range(10, -1, -1):
            sub = []
            for j in range(len(result)):
                sub.append(result[j][i])
            if sub.count(max(sub)) != len(result):
                result = result[sub.index(max(sub))]
                break

    return result


print(solution(n, info))