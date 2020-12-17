# 11651번 : 좌표 정렬하기 2
import sys
input = sys.stdin.readline

n = int(input())

array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append([y, x])

s_array = sorted(array)

for y, x in s_array:
    print(x, y)

"""
# 두번째 출력방법
for i in range(n):
    print(s_array[i][1], s_array[i][0])
"""