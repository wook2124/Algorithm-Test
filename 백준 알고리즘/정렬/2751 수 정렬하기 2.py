# 2751번 : 수 정렬하기 2

# 풀이 1
n = int(input())
ls = []

for _ in range(n):
    ls.append(int(input()))

s = sorted(ls)

for i in s:
    print(i)

# 풀이 2
n = int(input())
ls = []

for i in range(n):
    ls.append(int(input()))

for i in reversed(ls):
    print(i)