# 1065번 : 한수
n = int(input())
hansu = 0

for i in range(1, n + 1):
    if i < 100:             # 1부터 99까지는 모두 한수
        hansu += 1
    else:                   # 100부터는, ex) 123 -> 3 - 2 =  2 - 1
        n_str = list(map(int, str(i)))
        if n_str[2] - n_str[1] == n_str[1] - n_str[0]:
            hansu += 1

print(hansu)