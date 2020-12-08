# 10844번 : 쉬운 계단 수
import sys
input = sys.stdin.readline

# make dp
dp = []
dp.append([1 for i in range(10)])
for i in range(99):
  dp.append([0 for i in range(10)])

# iterate dp
for i in range(99):
  for j in range(10):
    if j >= 1:
      dp[i + 1][j - 1] += dp[i][j]
    if j <= 8:
      dp[i + 1][j + 1] += dp[i][j]

# input & output
n = int(input())
print((sum(dp[n - 1]) - dp[n - 1][0]) % 1000000000)