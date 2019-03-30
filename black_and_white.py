##Пиксели рисунка закодированы числами от 0 до 255 (обозначающими яркость пикселей) в виде матрицы, содержащей N строк и M столбцов. Нужно преобразовать рисунок в черно-белый по следующему алгоритму:
##1) вычислить среднюю яркость пикселей по всему рисунку;
##2) все пиксели, яркость которых меньше средней, сделать черными (записать код 0), а остальные – белыми (код 255).
##
##Пример:
##
##Матрица А:
##12 14 67 45
##32 87 45 63 
##69 45 14 11
##40 12 35 15
##Средняя яркость 37.88
##
##Результат:
##0 0 255 255
##0 255 0 255
##255 255 0 0
##255 0 0 0
n = int(input('The length of 2d array is '))
m = int(input('The width of the array '))
a = []
for i in range(n):
    a.append([int(j) for j in input('Input {} numbers of the array '.format(m)).split()])
print('Now array looks like this:')
for b in a:
    for j in b:
        print(j, end = ' ')
    print()
i = 0
sum = 0
for b in a:
    for j in b:
       sum += j
       i += 1
mid = sum//i

#changing to black and white version
for b in range(m):
    for j in range(n):
        if a[b][j] > mid:
            a[b][j] = 255
        else:
            a[b][j] = 0
            

print('Now it looks like this: ')

for b in a:
    for j in b:
        print(j, end = ' ')
    print()
    
#переделать в функции