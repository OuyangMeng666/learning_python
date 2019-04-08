import random
n = int(input("Input a number of numbers for guessing "))
print("Sasha has guessed a number from 1 to {}".format(n))
answer = random.randint(1, n)
s = set()
all_num = [a+1 for a in range(n)]
all_num = set(all_num)
yes_num = set()
no_num = set()
for i in range(random.randint(1, 10)):
    for b in range(random.randint(1, 5)):
       s.add(random.randint(2, n)) 
    print("Anya's guess is", end = " ")
    for x in s:
            print(x, end = " ")
    if answer in s:
        yes_num = yes_num|s
        print()
        print("Sasha says Yes")
    else:
        no_num = no_num|s
        print()
        print("Sasha says No")
    s = set()
print('Help')
if yes_num:
    if len(yes_num - no_num) == 1:
        print("I know the answer! It's ", end = " ")
        for i in yes_num - no_num:
            print(i, end = " ")
    else:
        print("The right answer is among these numbers ", end = " ")
        for i in yes_num - no_num:
            print(i, end = " ")
else:
    if len(all_num - no_num) == 1:
        print("I know the answer! It's ", end = " ")
        for i in all_num - no_num:
            print(i, end = " ")
    else:
        print("The right answer is among these numbers", end = " ")
        for i in all_num - no_num:
            print(i, end = " ")
