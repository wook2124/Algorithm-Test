# 1924번 : 2007년
day = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON","TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x - 1):
    day += month[i]

day = (day + y) % 7

print(week[day])


# calender module 사용하기
import calendar
week = ["MON","TUE", "WED", "THU", "FRI", "SAT", "SUN"]

x, y = map(int, input().split())

day = calendar.weekday(2007, x, y)
print(week[day])