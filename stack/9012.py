import sys
sys.stdin = open('9012.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(input())

    result = 'YES'
    s_cnt = 0
    e_cnt = 0

    for i in data:
        if i == "(":
            if s_cnt >= e_cnt:
                s_cnt += 1
            else:
                result = "NO"
        else:
            if s_cnt >= e_cnt:
                e_cnt += 1
            else:
                result = "NO"
    if s_cnt == e_cnt and result == 'YES':
        print('YES')
    else:
        print("NO")
