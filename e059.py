#from script.cipher1 import cipher
def Euler_59():
    cipher = []
    with open('script/cipher1.txt') as f:
        tmp = [i.split(',') for i in f.read().split('\n')[1:-1]]
        cipher.extend(tmp)
    cipher = [int(i) for i in cipher[0]]
    string =  'abcdefghijklmnopqrstuvwxyz'
    pwrds = [i+j+k for i in string for j in string for k in string]
    for p in pwrds:    
        pwrd = [ord(a) for a in p]
        l = len(pwrd)
        nums = [c^pwrd[x%l] for x,c in enumerate(cipher)]
        text = ''.join(chr(f) for f in nums)
        if text.find(' the ')>0:
            words = ''.join([chr(x) for x in nums])
            print(words)
            return sum(nums)
    '''
    for num in aset:
        for i in range(100):
            if num^i==ord(' '):
                x = [c^i for c in test]
                y = ''.join(chr(p) for p in x)
                y = y.lower()
                n = y.find('the')
                print(y)
                if n>0:print(y);print(ord(y[n]))
                if y.find('\ the')>0:return sum(x)
    '''
    return 'nope'


if __name__=='__main__':
    print(Euler_59())

