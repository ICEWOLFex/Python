import calendar
yourYear = int(input("Введите год "))
year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if calendar.isleap(yourYear):
    year[1] = 29
else:
    year[1] = 28

fulYearDays = 0
for month in range(12):
    for days in range(year[month] + 1):
        fulYearDays += days//10+days%10
print(fulYearDays)