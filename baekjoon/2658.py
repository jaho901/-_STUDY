import sys
sys.stdin = open('2658.txt')

# 직각 이등변 삼각형 조건
# 세 변 a, b, c가 존재한다.
# a == b, a*sqrt(2) == b*sqrt(2) == c
# a == b < c < 2*a == 2*b

data = [list(map(int, input())) for _ in range(10)]
vertex = []
max_x, max_y = 0, 0
max_x_value, max_y_value = 0, 0

for idx, i in enumerate(data):
    if i.count(1) == 1:
        vertex.append([idx, i.index(1)])
    if i.count(1) > max_x_value:
        max_x = idx
        max_x_value = i.count(1)


for idx, i in enumerate(zip(*data)):
    if i.count(1) == 1:
        vertex.append([i.index(1), idx])
    if i.count(1) > max_y_value:
        max_y = idx
        max_y_value = i.count(1)

if len(vertex) == 2:
    vertex.append([max_x, max_y])
vertex = sorted(vertex)

width, height = [], []
for x, y in vertex:
    width.append(x)
    height.append(y)
width_list = [0]*10
height_list = [0]*10
for i in range(10):
    width_list[i] = width.count(i)
    height_list[i] = height.count(i)
# 총 2가지 경우
# 1번 가로, 세로, 대각선(가장 긴)
if width_list.count(2) and height_list.count(2) and len(vertex)==3:
    break_check = False
    # 왼쪽 위가 대각선인 경우
    if vertex[0][0] == vertex[1][0] and vertex[0][1] == vertex[2][1] and vertex[0][0] < vertex[2][0] and vertex[0][1] < vertex[1][1]:
        diff = vertex[2][0] - vertex[0][0]
        range_list = list(range(diff, -1, -1))
        for i in range(vertex[0][0], vertex[0][0]+diff+1):
            for j in range(vertex[0][1], vertex[0][1]+range_list[i-vertex[0][0]]+1):
                if 0<=i<10 and 0<=j<10 and data[i][j] != 1:
                    break_check = True
                    break
        if not break_check:
            a = (vertex[0][1]-vertex[1][1])**2
            b = (vertex[0][0]-vertex[2][0])**2
            c = (vertex[1][0]-vertex[2][0])**2 + (vertex[1][1]-vertex[2][1])**2
            if a + b == c:
                for x, y in vertex:
                    print(x + 1, y + 1)
            else:
                print(0)
        else:
            print(0)
    # 오른쪽 위가 대각선인 경우
    elif vertex[0][0] == vertex[1][0] and vertex[1][1] == vertex[2][1] and vertex[0][1] < vertex[1][1] and vertex[1][0] < vertex[2][0]:
        diff = vertex[1][1] - vertex[0][1]
        range_list = list(range(diff, -1, -1))
        for i in range(vertex[0][0], vertex[0][0] + diff + 1):
            for j in range(vertex[1][1]-range_list[i-vertex[0][0]], vertex[1][1]+1):
                if 0<=i<10 and 0<=j<10 and data[i][j] != 1:
                    break_check = True
                    break
        if not break_check:
            a = (vertex[0][1] - vertex[1][1]) ** 2
            b = (vertex[1][0] - vertex[2][0]) ** 2
            c = (vertex[0][0] - vertex[2][0]) ** 2 + (vertex[0][1] - vertex[2][1]) ** 2
            if a + b == c:
                for x, y in vertex:
                    print(x + 1, y + 1)
            else:
                print(0)
        else:
            print(0)
    # 왼쪽 아래가 대각선인 경우
    elif vertex[2][0] == vertex[1][0] and vertex[0][1] == vertex[1][1] and vertex[0][0] < vertex[1][0] and vertex[1][1] < vertex[2][1]:
        diff = vertex[1][0] - vertex[0][0]
        range_list = list(range(diff+1))
        for i in range(vertex[0][0], vertex[0][0] + diff + 1):
            for j in range(vertex[1][1], vertex[1][1]+range_list[i-vertex[0][0]]+1):
                if 0<=i<10 and 0<=j<10 and data[i][j] != 1:
                    break_check = True
                    break
        if not break_check:
            a = (vertex[0][0] - vertex[1][0]) ** 2
            b = (vertex[1][1] - vertex[2][1]) ** 2
            c = (vertex[0][0] - vertex[2][0]) ** 2 + (vertex[0][1] - vertex[2][1]) ** 2
            if a + b == c:
                for x, y in vertex:
                    print(x + 1, y + 1)
            else:
                print(0)
        else:
            print(0)
    # 오른쪽 아래가 대각선인 경우
    elif vertex[0][1] == vertex[2][1] and vertex[1][0] == vertex[2][0] and vertex[0][0] < vertex[1][0] and vertex[0][1] > vertex[1][1]:
        diff = vertex[1][0] - vertex[0][0]
        range_list = list(range(diff + 1))
        for i in range(vertex[0][0], vertex[0][0] + diff + 1):
            for j in range(vertex[2][1]-range_list[i-vertex[0][0]], vertex[2][1]+1):
                if 0<=i<10 and 0<=j<10 and data[i][j] != 1:
                    break_check = True
                    break
        if not break_check:
            a = (vertex[0][0] - vertex[2][0]) ** 2
            b = (vertex[1][1] - vertex[2][1]) ** 2
            c = (vertex[0][0] - vertex[1][0]) ** 2 + (vertex[0][1] - vertex[1][1]) ** 2
            if a + b == c:
                for x, y in vertex:
                    print(x + 1, y + 1)
            else:
                print(0)
        else:
            print(0)


# 2번 대각선, 대각선, 가로(가장 긴) or 세로(가장 긴)
elif width_list.count(2) or height_list.count(2) and len(vertex)==3:
    # 가로가 가장 긴 경우
    if width_list.count(2):
        data = list(zip(*data))
        break_check = False
        # 꼭지점이 가로보다 위에 있는 경우
        if vertex[0][0] < vertex[1][0]:
            range_list = list(range(vertex[1][0] - vertex[0][0])) + [vertex[1][0] - vertex[0][0]] + list(
                range(vertex[1][0] - vertex[0][0] - 1, -1, -1))
            for i in range(vertex[1][1], vertex[2][1] + 1):
                for j in range(vertex[1][0] - range_list[i - vertex[1][1]], vertex[1][0]):
                    if 0<=i<10 and 0<=j<10 and data[i][j] != 1:
                        break_check = True
                        break
            if not break_check:
                a = (vertex[0][0] - vertex[1][0]) ** 2 + (vertex[0][1] - vertex[1][1]) ** 2
                b = (vertex[0][0] - vertex[2][0]) ** 2 + (vertex[0][1] - vertex[2][1]) ** 2
                c = (vertex[1][1] - vertex[2][1]) ** 2
                if a + b == c:
                    for x, y in vertex:
                        print(x + 1, y + 1)
                else:
                    print(0)
            else:
                print(0)
        # 꼭지점이 가로 밑에 있는 경우
        elif vertex[2][0] > vertex[1][0]:
            range_list = list(range(vertex[2][0] - vertex[0][0])) + [vertex[2][0] - vertex[0][0]] + list(
                range(vertex[2][0] - vertex[0][0] - 1, -1, -1))
            for i in range(vertex[0][1], vertex[1][1] + 1):
                for j in range(vertex[1][0], vertex[1][0] + range_list[i - vertex[0][1]]+1):
                    if 0<=i<10 and 0<=j<10 and data[i][j] != 1:
                        break_check = True
                        break
            if not break_check:
                a = (vertex[0][0] - vertex[2][0]) ** 2 + (vertex[0][1] - vertex[2][1]) ** 2
                b = (vertex[1][0] - vertex[2][0]) ** 2 + (vertex[1][1] - vertex[2][1]) ** 2
                c = (vertex[0][1] - vertex[1][1]) ** 2
                if a + b == c:
                    for x, y in vertex:
                        print(x + 1, y + 1)
                else:
                    print(0)
            else:
                print(0)
    # 세로가 가장 긴 경우
    elif height_list.count(2):
        range_list = list(range(vertex[1][0] - vertex[0][0])) + [vertex[1][0] - vertex[0][0]] + list(range(vertex[1][0] - vertex[0][0]-1, -1, -1))
        break_check = False
        # 꼭지점이 세로 왼쪽에 있는 경우
        if vertex[0][1] > vertex[1][1]:
            for i in range(vertex[0][0], vertex[2][0]+1):
                for j in range(vertex[0][1]-range_list[i-vertex[0][0]], vertex[0][1]):
                    if 0<=i<10 and 0<=j<10 and data[i][j] != 1:
                        break_check = True
                        break
        # 꼭지점이 세로 오른쪽에 있는 경우
        elif vertex[0][1] < vertex[1][1]:
            for i in range(vertex[0][0], vertex[2][0]+1):
                for j in range(vertex[0][1], vertex[0][1]+range_list[i-vertex[0][0]]):
                    if 0<=i<10 and 0<=j<10 and data[i][j] != 1:
                        break_check = True
                        break
        if not break_check:
            a = (vertex[0][0]-vertex[1][0])**2 + (vertex[0][1]-vertex[1][1])**2
            b = (vertex[2][0]-vertex[1][0])**2 + (vertex[2][1]-vertex[1][1])**2
            c = (vertex[0][0]-vertex[2][0])**2
            if a + b == c:
                for x, y in vertex:
                    print(x+1, y+1)
            else:
                print(0)
        else:
            print(0)
else:
    print(0)