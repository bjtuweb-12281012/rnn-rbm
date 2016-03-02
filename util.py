# convert a decimal (denary, base 10) integer to a binary string (base 2)
# tested with Python24   vegaseat    6/1/2005
import numpy

def Denary2Binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

def int2bin(n, count=14):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def bin2numpy(bin):
    dataset = numpy.zeros(14)
    for i in range(0,len(bin)):
        if bin[i] == '1':
            dataset[i] = 1
    return dataset
def mapnumpy(datasets):
    datasets2 = map(lambda x: bin2numpy(int2bin(x, 14)),datasets)

    return datasets2


# this test runs when used as a standalone program, but not as an imported module
# let's say you save this module as den2bin.py and use it in another program
# when you import den2bin the __name__ namespace would now be  den2bin  and the
# test would be ignored
if __name__ == '__main__':
    datasets = [16, 2562, 18, 16, 155, 126, 17, 25, 4, 63, 32, 278, 18, 2, 4702, 7, 134, 2963, 5, 1, 2, 1, 109, 112, 156, 6, 3694, 5, 371, 27, 4, 59, 6, 456, 40]
    print mapnumpy(datasets)