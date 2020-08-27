# a = input()   단어 1개, 문장 1개 입력받아
# print(a)      그대로 출력하기


# a, b = map(int, input().split('.'))
# print('%d\n%d' %(a, b))       실수 1개 입력받아        

# a, b = input().split('.')     부분별로 출력하기     
# print(a + "\n" + b)


# a = input()                   
# for i in range(len(a)) :  
#    print("'" + a[i] + "'")    단어 1개 입력받아

# a = input()                   
# for i in a :              
#     print("'" + i + "'")      나누어 출력하기

# 1025 정수 1개 입력받아 나누어 출력하기
# a = input()                 
# for i in range(len(a)):     
#     x = int(a[i])
#     n = (len(a)-i-1)
#     print([x*(10**n)])      

# a, b, c, d, e = map(int, input()) 나누어 출력하기
# print('[%d0000]\n[%d000]\n[%d00]\n[%d0]\n[%d]' % (a, b, c, d, e))


a, b, c = map(int, input().split(':'))
print(b)