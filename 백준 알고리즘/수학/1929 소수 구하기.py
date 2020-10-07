# 1929번 : 소수 구하기
def prime(num):
    if num < 2:
        return False
    
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

m, n = map(int, input().split())

for i in range(m, n + 1):
    if prime(i):
        print(i) 