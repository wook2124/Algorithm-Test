# 11650번 : 좌표 정렬하기
import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    [a, b] = map(int, input().split())
    array.append([a, b])

s_array = sorted(array)

for i in range(n):
    print(s_array[i][0], s_array[i][1])