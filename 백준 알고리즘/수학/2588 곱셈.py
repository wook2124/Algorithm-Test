# 2588번 : 곱셈
a = int(input())        # 472
b = int(input())        # 385

print(a * (b % 10))
print(a * ((b // 10) % 10))
print(a * (b // 100))
print(a * b)