# 2562번 : 최댓값
n = []

for _ in range(9):
    n.append(int(input()))

print(max(n), n.index(max(n)) + 1)