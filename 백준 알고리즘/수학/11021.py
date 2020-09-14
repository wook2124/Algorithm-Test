# 11021번 : A + B - 7
t = int(input())        # 5

for i in range(t):      # i = 0 ~ 4
    i += 1              # i = 1 ~ 5
    a, b = map(int, input().split())
    print("Case #%s: %s" %(i, a + b))