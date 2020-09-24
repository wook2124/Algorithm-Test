# 1463번 : 1로 만들기
x = int(input())
# x = 10

result = [0 for _ in range(x + 1)]
# result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1, x + 1):
    if i == 1:
        result[i] = 0
        continue
    
    result[i] = result[i - 1] + 1

    if i % 3 == 0 and result[i // 3] + 1 < result[i]:
        result[i] = result[i // 3] + 1

    elif i % 2 == 0 and result[i // 2] + 1 < result[i]:
        result[i] = result[i // 2] + 1
    '''
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0] i = 2
    [0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0] i = 3
    [0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0] i = 4
    [0, 0, 1, 1, 2, 3, 0, 0, 0, 0, 0] i = 5
    [0, 0, 1, 1, 2, 3, 4, 0, 0, 0, 0] i = 6
    [0, 0, 1, 1, 2, 3, 2, 3, 0, 0, 0] i = 7
    [0, 0, 1, 1, 2, 3, 2, 3, 4, 0, 0] i = 8
    [0, 0, 1, 1, 2, 3, 2, 3, 3, 4, 0] i = 9
    [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3] i = 10
    '''
    
print(result[x])