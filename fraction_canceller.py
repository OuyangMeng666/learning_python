def find_max(num, num1, num2):
    for i in range(num, 1, -1):
            if num1%i == 0 and num2%i == 0:
                print("Canceled fraction {}/{} to {}/{}".format(num1,num2,num1//i, num2//i))
                break
            
def cancel(num1, num2):
    '''takes nominator and denominator as input,
outputs cancelled fraction'''
    if num1 < num2:
        find_max(num1, num1, num2)
    else:
        find_max(num2, num1, num2)
        
##        for i in range(num1, 1, -1):
##            if num1%i == 0 and num2%i == 0:
##                print("Сократили дробь {}/{} до {}/{}".format(num1,num2,num1//i, num2//i))
##                break
##    else:
##        for i in range(num2, 1, -1):
##            if num1%i == 0 and num2%i == 0:
##                print("Сократили дробь {}/{} до {}/{}".format(num1,num2,num1//i, num2//i))
##                break

