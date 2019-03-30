months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#asks to input day and month of your date
a_list = input("Введите день и месяц даты через пробел ").split()
a = [int(i) for i in a_list]
days_of_months = 0
for i in range (a[1]-1):
    days_of_months += months[i]
until_ny = 365 - days_of_months - a[0]

day = until_ny%10
if day == 1:
    days = 'день'
if day == 3 or day == 4:
    days = 'дня'
else:
    days = 'дней'
if until_ny == 0:
    days = 'дней'
    
print('До нового года осталось: {0} {1}'.format(until_ny, days))
