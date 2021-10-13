import sys
sys.stdin = open('2467.txt')

N = int(input())
solution = list(map(int, input().split()))

'''
규칙이 존재한다!!!
어차피 용액은 음수 ~ 양수로 오름차순 정렬이 되어있다 (문제보면나옴)
가장 처음(s==0)과 가장 끝(e==N-1)에서 시작했을 때
용액의 합이 음수라면
==> s를 1씩 더한다.
용액의 합이 양수라면
==> e를 1씩 빼준다.
'''

s, e = 0, N-1
# 초기값 지정
result = abs(solution[s] + solution[e])
liquid = [solution[s], solution[e]]

while True:
    sub = solution[s] + solution[e]
    # 어차피 result는 위에서 절댓값 씌어서 여기서 abs쓸 필요없음
    if result > abs(sub):
        result = abs(sub)
        liquid = [solution[s], solution[e]]

    if sub < 0:
        s += 1
    elif sub > 0:
        e -= 1
    else:
        break
    if s >= e:
        break

print(liquid[0], liquid[1])

