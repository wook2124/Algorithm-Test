# 11651번 : 좌표 정렬하기 2
n = int(input())

array = []
for i in range(n):
    a, b = map(int, input().split())
    array.append([b, a])

s_array = sorted(array)

print(s_array)