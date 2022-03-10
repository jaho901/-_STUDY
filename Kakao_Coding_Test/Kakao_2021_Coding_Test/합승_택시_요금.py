
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

# n = 7
# s = 3
# a = 4
# b = 1
# fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

# n = 6
# s = 4
# a = 5
# b = 6
# fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

import heapq

def solution(n, s, a, b, fares):
    node = [[] for _ in range(n+1)]
    for u, v, w in fares:
        node[u].append([w, v])
        node[v].append([w, u])

    def dijkstra(s):
        visited = [999999999] * (n + 1)
        visited[s] = 0
        heap = []
        heapq.heappush(heap, [0, s])
        while heap:
            w, v = heapq.heappop(heap)

            for nw, nv in node[v]:
                new_weight = w + nw
                if visited[nv] > new_weight:
                    visited[nv] = new_weight
                    heapq.heappush(heap, [new_weight, nv])
        return visited

    data = [[]] + [dijkstra(i) for i in range(1, n+1)]

    result = 999999999

    for i in range(1, n+1):
        result = min(result, data[s][i] + data[i][a] + data[i][b])

    return result


print(solution(n, s, a, b, fares))