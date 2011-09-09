import re
with open('script/roman.txt') as f:
    alist = list(x for x in f.read().split('\n')[1:])
pattern = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
roman = {'M':  1000,
         'CM':900,
         'D': 500,
         'CD':400,
         'C': 100,
         'XC':90,
         'L': 50,
         'XL':40,
         'X': 10,
         'IX':9,
         'V': 5,
         'IV':4,
         'I': 1}   
roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1)) 
def Euler_89():
    length = 0
    count = 0
    for i in alist:
        length+=len(i)
        nums = to_num(i)
        n = to_rom(nums)
        count+=len(n)
    return length-count

def to_rom(num):
    result = ''
    for numeral, integer in roman_numeral_map:
        while num >= integer:
            result += numeral
            num -= integer
    return result

def to_num(i):
    j = 0
    ret = 0
    while len(i):
        if len(i)>=2 and roman.get(i[j:j+2]):
            ret += roman.get(i[j:j+2]);i = i[2:]
        else:ret+=roman.get(i[j]);i = i[1:]
    return ret
        

if __name__=='__main__':
    print(Euler_89())
