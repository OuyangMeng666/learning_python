n = int(input('Input the length of the array ')) 
a = []
for i in range(n):
    a.append([int(j) for j in input('Input numbers for the list ').split()])
print('Now the array looks like this:')
for i in a:
    for j in i:
        print(j, end = ' ')
    print()

min = a[0][0]
max = a[0][0]
min_index = 0
max_index = 0

for i in range(n):
    for j in range(n):
        if a[i][j] > max:
            max = a[i][j]
            max_index = j
        if a[i][j] < min:
            min = a[i][j]
            min_index = j
            
print('Column with minimal value ', min_index, ', column with max value', max_index)

#changing columns with minimal and maximum values
for i in a:
    i[min_index], i[max_index] = i[max_index], i[min_index]

print('Now our array looks like this:')
for i in a:
    for j in i:
        print(j, end = ' ')
    print()
