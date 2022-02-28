# rows = 6
# columns = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

# rows = 3
# columns = 3
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

# rows = 100
# columns = 97
# queries = [[1,1,100,97]]

from collections import deque

def solution(rows, columns, queries):
    matrix = [[0]*columns for _ in range(rows)]
    x, y, i = 0, 0, 1
    while True:
        if y < columns:
            matrix[x][y] = i
            y += 1
            i += 1
        else:
            x += 1
            y = 0
            matrix[x][y] = i
            y += 1
            i += 1
        if i > rows*columns:
            break

    def rotate(s_x, s_y, e_x, e_y):
        queue = deque()
        dx, dy, k = [0, 1, 0, -1], [1, 0, -1, 0], 0
        x, y = s_x, s_y
        # queue에 담기
        queue.append(matrix[x][y])
        while True:
            nx, ny = x+dx[k], y+dy[k]
            if nx == s_x and ny == s_y:
                break
            if s_x <= nx <= e_x and s_y <= ny <= e_y:
                queue.append(matrix[nx][ny])
                x, y = nx, ny
            else:
                k += 1
        # 시계방향 회전하기
        queue.rotate(1)
        min_num = min(queue)
        # matrix에 변경하기
        x, y, k  = s_x, s_y, 0
        matrix[x][y] = queue.popleft()
        while queue:
            nx, ny = x+dx[k], y+dy[k]
            if s_x <= nx <= e_x and s_y <= ny <= e_y:
                matrix[nx][ny] = queue.popleft()
                x, y = nx, ny
            else:
                k += 1
        return min_num

    result = []
    for s_x, s_y, e_x, e_y in queries:
        result.append(rotate(s_x-1, s_y-1, e_x-1, e_y-1))

    return result

print(solution(rows, columns, queries))