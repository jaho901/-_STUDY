
# no = "예1"
# new_id = "...!@BaT#*..y.abcdefghijklm"

# no = "예2"
# new_id = "z-+.^."

no = "예3"
new_id = "=.="

# no = "예4"
# new_id = "123_.def"

# no = "예5"
# new_id = "abcdefghijklmn.p"

def solution(new_id):
    result = ""
    for i in range(len(new_id)):
        # 1단계
        if new_id[i].isalpha():
            result += new_id[i].lower()
        # 2단계
        elif new_id[i].isnumeric() or new_id[i]=='-' or new_id[i]=='_' or new_id[i]=='.':
            result += new_id[i]
    sub_result = result[0]
    # 3단계
    for i in range(1, len(result)):
        if sub_result[-1] == '.' and result[i] == '.':
            pass
        else:
            sub_result += result[i]
    # 4단계
    if sub_result[0] == '.':
        sub_result = sub_result[1:]
    if len(sub_result) >= 1 and sub_result[-1] == '.':
        n = len(sub_result)
        sub_result = sub_result[:n-1]
    # 5단계
    if len(sub_result) == 0:
        sub_result = 'a'
    # 6단계
    if len(sub_result) >= 16:
        sub_result = sub_result[:15]
        while True:
            if sub_result[-1] == '.':
                sub_result = sub_result[:-1]
            else:
                break
    # 7단계
    if len(sub_result) <= 2:
        while True:
            sub = sub_result[-1]
            sub_result += sub
            if len(sub_result) == 3:
                break

    return sub_result

print(solution(new_id))