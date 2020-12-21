# 11004번 : K번째 수
n, k = map(int, input().split())

a = list(map(int, input().split()))

result = sorted(a)

print(result[k - 1])