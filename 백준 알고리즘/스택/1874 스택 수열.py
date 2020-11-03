# 1874번 : 스택 수열
n = int(input())
stack = []
result = []
count = 0
X = True

for _ in range(n):
    num = int(input())

    while count < num:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        X = False
        break

if X == False:
    print("NO")
else:
    for i in result:
        print(i)