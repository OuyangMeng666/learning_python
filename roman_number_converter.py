##Напишите программу, которая получает натуральное число, а выводит на экран запись переданного числа в римской
##системе счисления. 
##
##Справка - римские цифры:
##I = 1 
##V = 5
##X = 10
##L = 50
##C = 100
##D = 500
##M = 1000
##
##Учтите, что 4 записывается как IV, 9 - как IX, 40 - как XL и т.д.
#max3999
a = str(input('Arabic numbers to latin converter. Please input your number up to 3999 '))
old_a = a
num = ''
if len(a) < 4:
    a = ('0' * (4-(len(a)))) + a
    #1(0)0(1)0(2)0(3)
    
if a[0] == '1':
        num += 'M'
if a[0] == '2':
        num += 'MM'
if a[0] == '3':
        num += 'MMM'
    
if '9' > a[1] > '4':
        num += 'D'
if a[1] == '6' or a[1] == '1':
        num += 'C'
if a[1] == '7' or a[1] == '2':
        num += 'CC'
if a[1] == '8' or a[1] == '3':
        num += 'CCC'
if a[1] == '4':
        num += 'CD'
if a[1] == '9':
        num += 'CM'
    
if '9' > a[2] > '4':
        num += 'L'
if a[2] == '6' or a[2] == '1':
        num += 'X'
if a[2] == '7' or a[2] == '2':
        num += 'XX'
if a[2] == '8' or a[2] == '3':
        num += 'XXX'
if a[2] == '4':
        num += 'XL'
if a[2] == '9':
        num += 'XC'
        
if '9' > a[3] > '4':
        num += 'V'
if a[3] == '6' or a[3] == '1':
        num += 'I'
if a[3] == '7' or a[3] == '2':
        num += 'II'
if a[3] == '8' or a[3] == '3':
        num += 'III'
if a[3] == '4':
        num += 'IV'
if a[3] == '9':
        num += 'IX'
    
print('Converted your number ', old_a, 'to roman number: ', num)