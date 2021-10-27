# UF



### 1. 부모리스트를 생성

```python
parent = list(range(n+1))
```





### 2. Find 함수 지정

```python
def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])
```



```python
# path compression
def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
```

> 시간복잡도를 줄이기 위한 하나의 방법





### 3. Union 함수 지정

```python
def union(x, y):
    a = find(x)
    b = find(y)
    parent[b] = a
```



```python
# union by rank
def union(x, y):
    a = find(x)
    b = find(y)

    # 랭크가 더 큰 쪽 밑에 작은 부분을 다 합치는거야
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1
```

> 시간복잡도를 줄이기 위한 하나의 방법





#### UF를 사용한 알고리즘

1. MST 알고리즘

   > 일단 모든 노드들을 연결을 할건데 **가중치 합이 최소**가 되도록 연결  ->  결과의 여부 확인



2. 크루스칼 알고리즘

   > 가중치를 우선적으로 오름차순  ->  처음부터 끝까지 연결하면서 계산
   >
   > 자연스럽게 가중치 합이 최소가 되게 연결이 된다!

































