# 2579번 : 계단 오르기
import sys
input = sys.stdin.readline

stair = []
dp = []

n = int(input())
for _ in range(i):
    stair.append(int(input()))

dp.append(stair[0])
dp.append(max(stair[0] + stair[1], stair[1]))
dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
for i in range(3, n):
    dp.append(max(dp[i - 2] + stair[i], dp[i - 3] + stair[i] + stair[i - 1]))

print(dp.pop())