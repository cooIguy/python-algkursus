import datetime

now = datetime.datetime.now()

print(now.year) #kuvab praeguse aasta (2025)
print(now.month) #kuvab praeguse kuu numbri (1-12)
print(now.day) #kuvab praeguse kuupäeva numbri (1-31)
print(now.hour) #kuvab praeguse tunni (0-23)

weekday = now.strftime("%A")
print(weekday)