# 10828번 : 스택
import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    i = sys.stdin.readline().split()

    if i[0] == 'push':
        stack.append(int(i[1]))
    
    elif i[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    
    elif i[0] =='size':
        print(len(stack))

    elif i[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif i[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])