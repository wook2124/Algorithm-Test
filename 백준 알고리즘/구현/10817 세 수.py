# 10817번 : 세 수
# 풀이 1
a, b, c = map(int, input().split())
x = []
x.append(a)
x.append(b)
x.append(c)

result = sorted(x, reverse = True)

print(result[1])

# 풀이 2
L = list(input().split())

for i in range(len(L)):
    L[i] = int(L[i])

sorted_L = sorted(L, reverse = True)
print(sorted_L[1])