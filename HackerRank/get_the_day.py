import calendar as cal

m, d, y = map(int, input().split())
day = cal.weekday(year=y, month=m, day=d)
print(cal.day_name[day].upper())
