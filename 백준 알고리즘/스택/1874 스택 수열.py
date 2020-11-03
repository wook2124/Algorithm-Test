# 1874번 : 스택 수열
n = int(input())
stack = []
result = []
count = 0
possible = True

for _ in range(n):
    num = int(input())

    while count < num:
        count += 1
        stack.append(count)
        result.append("+")

    top = stack[-1]
    if top == num:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break

if possible == False:
    print("NO")
else:
    for i in result:
        print(i)