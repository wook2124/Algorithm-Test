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
