# 10872번 : 팩토리얼
def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)

n = int(input())
print(fact(n))