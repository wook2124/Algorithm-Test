# 구구단 만들기 (1단 ~ 9단)
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i * j)
        if j == 9:
            print("")