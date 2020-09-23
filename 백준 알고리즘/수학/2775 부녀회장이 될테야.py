# 2775번 : 부녀회장이 될테야
t = int(input())                        # t = 2

for _ in range(t):
    k = int(input())                    # k = 1, 2
    n = int(input())                    # n = 3, 3
    num = [i for i in range(1, n + 1)]  # [1, 2, 3], [1, 2, 3]
    for _ in range(k):
        for i in range(1, n):
            num[i] += num[i - 1]        # [1, 3, 6] -> [1, 4, 10]
    print(num[-1])