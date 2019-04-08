#Gets three lists with items and prices (separated by spaces).
#Outputs all items with prices in alphabetical order.
#If the lists contain same items, the priority price would be the highest

list1 = input("Input the pricelist number 1\n").split()
list2 = input("Input the pricelist number 2\n").split()
list3 = input("Input the pricelist number 3\n").split()

dic = {}

def adding_to_dic(list):
    for i in range(len(list)):
        if 'a' < list[i] < 'z':
            if list[i] not in dic:
                dic[list[i]] = 0
        if '1' < list[i] < '9':
            if dic[list[i-1]] != 0:
                dic[list[i-1]] = max(dic[list[i-1]], list[i])
            dic[list[i-1]] = list[i]
            
adding_to_dic(list1)
adding_to_dic(list2)
adding_to_dic(list3)

total_list = list(dic.keys())
total_list.sort()

for i in total_list:
    print(i, dic[i])