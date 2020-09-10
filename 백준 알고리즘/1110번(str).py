n = input()    # "26"
num = n
cnt = 0

while 1:
   if len(num) == 1:
      num = "0" + num
   plus = str(int(num[0]) + int(num[1]))   # 2 + 6 = "8"
   num = num[-1] + plus[-1]    # "6" + "8" = "68"
   cnt += 1
   if num == n:
      print(cnt)
      break
