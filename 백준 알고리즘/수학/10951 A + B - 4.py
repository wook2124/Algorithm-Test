# 10951번 : A + B - 4
# 풀이 1
while 1:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# 풀이 2
try:
    while 1:
        a, b = map(int, input().split())
        print(a + b)
except:
    exit()