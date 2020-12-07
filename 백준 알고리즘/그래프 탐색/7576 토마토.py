# 7576번 : 토마토
import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())

arr = []
deq = deque()
visit = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    arr.append([*map(int, input().split())])

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            deq.append((i, j))
            visit[i][j] = 1

'''
한 번 배열 전체를 순회하면서 안 익은 토마토가 있는지 확인 한다.
익은 토마토는 존재하고, 안 익은 토마토가 없다면
처음부터 모든 토마토가 익은 상태이기 때문에 0을 출력한다.
'''
flag = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flag = 0
            break

if flag and deq:
    print(0)
    exit(0)

'''
모든 토마토가 익지 않았다면 하루(단계)를 카운트 하면서 BFS를 수행한다.
이 떄 모든 점을 순회하는게 아니라 익은 토마토를 기준으로, 해당 토마토에게
영향을 받는 부분에 대해서만 BFS를 진행한다.
'''
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

while 1:
    deq_second = deque()
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if not(0 <= new_x < n and 0 <= new_y < m): continue
            if visit[new_x][new_y] or arr[new_x][new_y] != 0: continue
            deq_second.append((new_x, new_y))
            visit[new_x][new_y] = 1
            arr[new_x][new_y] = 1
    deq = deq_second
    if not deq: break
    ans += 1

#아직 익지 않은 토마토가 있는지 확인하다.
for i in range(n):
    if 0 in arr[i]:
        print(-1)
        exit(0)
print(ans)