words = {
           1: ['one'             ] ,
           2: ['two'             ] ,
           3: ['three'           ] ,
           4: ['four'            ] ,
           5: ['five'            ] ,
           6: ['six'             ] ,
           7: ['seven'           ] ,
           8: ['eight'           ] ,
           9: ['nine'            ] ,
          10: ['ten'             ] ,
          11: ['eleven'          ] ,
          12: ['twelve'          ] ,
          13: ['thirteen'        ] ,
          14: ['fourteen'        ] ,
          15: ['fifteen'         ] ,
          16: ['sixteen'         ] ,
          17: ['seventeen'       ] ,
          18: ['eighteen'        ] ,
          19: ['nineteen'        ] ,
          20: ['twenty'          ] ,
          30: ['thirty'          ] ,
          40: ['forty'           ] ,
          50: ['fifty'           ] ,
          60: ['sixty'           ] ,
          70: ['seventy'         ] ,
          80: ['eighty'          ] ,
          90: ['ninety'          ] ,
         100: ['hundred'         ] ,
        1000: ['thousand'        ] ,
        }

def spell(num):
    word=[]
    if num//1000:
        a = num//1000
        word.extend(words[a])
        word.extend(words[1000])
        num%=1000
        if num:word.extend('and')
    if num//100:
        hundreds = num//100
        word.extend(words[hundreds])
        word.extend(words[100])
        num%=100
        if num:word.extend('and')
    tens = num
    ones = num%10
    if tens<20 and tens:
        word.extend(words[tens])
    else:
        if tens:tens -= ones
        if ones:word.extend(words[ones])
        if tens:word.extend(words[tens])
    return (word)

def Euler_17(first=1,last=1000):
    ret = sum(len(x) for n in range(first,last+1) for x in spell(n))
    return ret


if __name__=='__main__':
    print(Euler_17())
