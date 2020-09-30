# 10989번 : 수 정렬하기 3
import sys
n = int(input())
check_ls = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    check_ls[num] = check_ls[num] + 1

for i in range(10001):
    if check_ls[i] != 0:
        for _ in range(check_ls[i]):
            print(i)