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
# oneDays = (1*13+2*12+3*5+4*3+5*3+6*3+7*3+8*3+9*3)*7
# zeroDays =(1*12+2*12+3*4+4*3+5*3+6*3+7*3+8*3+9*3)*4
# if feb == 29:
#    febDays = 1*12+2*12+3*3+4*3+5*3+6*3+7*3+8*3+9*3
# elif feb == 28:
#     febDays = 1*12+2*11+3*3+4*3+5*3+6*3+7*3+8*3+9*2
# else:
#     print("Error")

# fulYearDays = oneDays+zeroDays+febDays
print(fulYearDays)
