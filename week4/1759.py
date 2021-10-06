import sys
sys.stdin = open('1759.txt')

L, C = map(int, input().split())
string = list(input().split())
string = sorted(string)
visited = [False] * C
sub = []
# print(''.join(string))
def recur(cur, cnt):
    # 재귀 깊이가 L까지 왔으면 그때 모음과 자음수를 계산해서 조건에 만족하면 제출
    if cur == L:
        vowel = 0
        consonant = 0
        for i in sub:
            if i in 'aeiou':
                vowel += 1
            else:
                consonant += 1
        if vowel >= 1 and consonant >= 2:
            print(''.join(sub))
        return

    # for문을 돌리면서 방문처리와 sub에 추가해주고 재귀를 빠져나오면 다시 원래대로 처리!! (조합)
    for j in range(cnt, len(string)):
        if not visited[j]:
            sub.append(string[j])
            visited[j] = True
            recur(cur+1, j+1)
            sub.pop(-1)
            visited[j] = False

recur(0, 0)

'''
조합 ( 중복x, 순서대로 )
recur(cur, cnt)

# 종료조건
if cur == N:
    ~~~

for 반복문 in range(cnt, N):
    if 방문 x :
        원하는 행위(ex) append or +)
        방문처리
        재귀
        위의 행위 취소 (ex) pop or -)
        방문취소

'''