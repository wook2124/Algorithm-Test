# 2750번 : 수 정렬하기
n = int(input())
ls = []

for _ in range(n):
    ls.append(int(input()))

s = sorted(ls)

for i in s:
    print(i) 