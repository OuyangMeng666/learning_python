s = input("Write a text string here ")
all_val = set()
bi_code = []
s_list = []
out_string = ''

def intoBinary(number):
    if (number!=0):
        while (number>=1):
            if (number %2==0):
                bi_code.append(0)
                number=number/2
            else:
                bi_code.append(1)
                number=(number-1)/2

    else:
        bi_code.append(0)
    bi_code.reverse()

for i in s:
    s_list.append(i)

for i in range(len(s)**2-1, 0, -1):
    intoBinary(i)
    if len(bi_code) < len(s_list):
        for i in range(len(s_list) - len(bi_code)):
            bi_code.insert(0, 0)
    for x in range(len(s_list)):
        if bi_code[x] == 1:
            out_string += str(s_list[x])
    if out_string:
        all_val.add(out_string)
        out_string = ''
    else:
        all_val.add(s)
    bi_code = []

for i in all_val:
    print(i, sep = " ", end = " ")
    
    
        