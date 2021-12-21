import sys
sys.stdin = open('2580.txt')

'''
1. 각각의 가로줄과 세로줄에는 1과 9의 숫자가 한번씩만
2. 3X3안에도 1부터 9까지의 숫자가 한번씩만
'''

sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

exist = False


def check_number(x, y):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 각 줄 check
    for num in range(9):
        # 해당 열 확인
        if sudoku[x][num] in numbers:
            numbers.remove(sudoku[x][num])
        # 해당 행 확인
        if sudoku[num][y] in numbers:
            numbers.remove(sudoku[num][y])

    # 예로 4,5 -> 0,1,2 / 3,4,5 / => 3~5 까지 확인
    # 3X3 확인
    for i in range(x//3*3, x//3*3+3):
        for j in range(y//3*3, y//3*3+3):
            if sudoku[i][j] in numbers:
                numbers.remove(sudoku[i][j])

    return numbers


def dfs(length):
    global exist

    # 이미 완료 된 경우
    if exist == True:
        return

    # 마지막
    if length == len(blank):
        for i in sudoku:
            print(*i)
        exist = True
        return

    else:
        (x, y) = blank[length]
        numbers = check_number(x, y)

        for num in numbers:
            sudoku[x][y] = num
            dfs(length + 1)
            sudoku[x][y] = 0

dfs(0)