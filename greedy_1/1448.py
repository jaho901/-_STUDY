import sys
sys.stdin = open('1448.txt')

N = int(input())
number = []
for _ in range(N):
    number.append(int(input()))
# 정렬시키기
number = sorted(number)

# for문을 통한 그리디
result = False
# 뒤에서부터 탐색
for i in range(len(number)-1, 1, -1):
    # 만약 가장 큰 수보다 2, 3번째로 큰수의 합이 크다면 => 삼각형이 만들어진다.
    if number[i] < number[i-1] + number[i-2]:
        # 조건을 만족하면 세 변의 합을 반환
        print(number[i] + number[i-1] + number[i-2])
        result = True
        break
# 위의 조건을 만족하지 않았으므로 -1 반환
if result == False:
    print(-1)
    
# while문을 통한 그리디
while True:
    if number[-1] >= number[-2] + number[-3]:
        if len(number) > 3:
            number.pop()
        elif len(number) == 3:
            print(-1)
            break
    else:
        print(number[-1] + number[-2] + number[-3])
        break