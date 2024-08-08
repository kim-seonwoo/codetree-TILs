n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(m)
]
count = 0

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def dfs(vertex):
    for curr_v in graph[vertex]:  # 올바른 리스트 인덱싱 사용
        if not visited[curr_v]:
            global count
            count += 1
            visited[curr_v] = True
            dfs(curr_v)

# 간선 정보를 이용해 그래프를 구축
for edge in grid:
    graph[edge[0]].append(edge[1])

root_vertex = 1  # 시작 정점을 1로 설정
visited[root_vertex] = True
dfs(root_vertex)

print(count)