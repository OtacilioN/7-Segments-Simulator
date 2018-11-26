import binascii
fo = open("hexvalues.txt", "r")
files = fo.read().splitlines()
a = 0 
for word in files:
    if(a%2):
        dec_data = int(word, 16)
        bin_data = bin(dec_data)
        print('(', end=' ')
        for x in range(7, 1, -1):
            value = bin_data[-x:(-x+1)]
            if(not value.isnumeric()):
                value = 0
            print(value, end=', ')
        value = bin_data[-1:]
        if(not value.isnumeric()):
            value = 0
        print(value, end='')
        print(")")

    a+=1


fo.close()