import sys
sys.stdin = open('2659.txt')


order = [0,1,2,3]*4

def dfs(data_list):
    sub=list(map(int,str(data_list)))
    for i in range(4):
        min_value = int(sub[order[i+1]]*1000 + sub[order[i+2]]*100 + sub[order[i+3]]*10 + sub[order[i]])
        if data_list > min_value:
            data_list = min_value
    return data_list

data = dfs(int(''.join(input().split())))
cnt=0
for i in range(1111, data+1):
    zero=list(map(int,str(i)))
    if 0 not in zero:
        if dfs(i)==i:
            cnt += 1
print(cnt)