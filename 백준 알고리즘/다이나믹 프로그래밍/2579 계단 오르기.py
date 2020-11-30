# 2579번 : 계단 오르기
import sys
input = sys.stdin.readline

n = int(input())
max_score = [0 for _ in range(n)]

# [10, 20, 15, 25, 10, 20]
steps = []
for i in range(n):
    steps.append(int(input()))

def score(n):
    # 첫 번째 계단, 10
    max_score[0] = steps[0]
    if n == 1:
        return
    
    # 두 번째 계단의 최댓값은 두 계단 모두를 밟을 때, 30
    max_score[1] = steps[1] + steps[0]
    if n == 2:
        return

    # 세 번째 계단은 1, 3 vs 2, 3 중 큰 수, 25 vs 35
    max_score[2] = max(steps[0] + steps[2], steps[1] + steps[2])
    if n == 3:
        return
    for i in range(3, n):
        # 마지막에서 치면 전계단에서 도착했을 때와
        # 전전 계단에서 도착했을 때를 비교하면 됌
        max_score[i] = steps[i] + max(steps[i - 1] + max_score[i - 3], max_score[i - 2])

score(n)
print(max_score[n - 1]) 