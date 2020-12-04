# 1920번 : 수 찾기
"""
n = int(input())
N = set(map(int, input().split()))

m = int(input())
M = set(map(int, input().split()))

result = N & M

print(result)
"""
import sys

n = int(sys.stdin.readline())
N = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

for i in M:
    if i in N:
        print(1)
    else:
        print(0)