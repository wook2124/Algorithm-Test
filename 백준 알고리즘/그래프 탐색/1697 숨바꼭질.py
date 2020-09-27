# 1697번 : 숨바꼭질
from collections import deque

def bfs():
    q = deque()             # deque는 양쪽에서 입출력 가능
    q.append(n)             # q = deque([5])
    while  q:
        x = q.popleft()     # 처음 시작점은 x = 5, q = deque([])
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):    # nx = 4, 6, 10
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)    # q = deque([4, 6, "10"])

MAX = 10 ** 5               # 시간초과 안나게 수 제한
dist = [0] * (MAX + 1)      # 이동하는 거리를 알기 위한 변수
n, k = map(int, input().split())

bfs()