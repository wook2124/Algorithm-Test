# 1260번 : DFS와 BFS
n, m, v = map(int, input().split()) # 4, 5, 1

matrix = [[0] * (n + 1) for i in range(n + 1)]
'''
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
'''

for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
'''
   0  1  2  3  4
0[[0, 0, 0, 0, 0],
1 [0, 0, 1, 1, 1],
2 [0, 1, 0, 0, 1],
3 [0, 1, 0, 0, 1],
4 [0, 1, 1, 1, 0]]
'''

visit = [0] * (n + 1)
# [0, 0, 0, 0, 0]

def dfs(v):
    visit[v] = 1    # 방문한 점 1로 표시
    print(v, end = " ")
    for i in range(1, n + 1):
        if (visit[i] == 0) and (matrix[v][i] == 1):
            dfs(i)

def bfs(v):
    queue = [v]     # 들려야 할 정점 저장
    visit[v] = 0    # 방문한 점 0으로 표시
    while queue:
        v = queue.pop(0)
        print(v, end = " ")
        for i in range(1, n + 1):
            if (visit[i] == 1) and (matrix[v][i] == 1):
                queue.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)