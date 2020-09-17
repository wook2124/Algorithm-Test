# 10818번 : 최소, 최대
# 풀이 1
n = int(input())
m = list(map(int, input().split()))
s = sorted(m)

print(s[0], s[-1])

# 풀이 2
n = int(input())
m = list(map(int, input().split()))
m.sort()

print(m[0], m[-1])