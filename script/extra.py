class elist(list):
    def __init__(self,*alist):
        if len(alist)==1:
            if type(alist[0])==type(range(1,2)):
                self.extend(list(alist[0]))
            elif type(alist[0])==type(' '):
                self.extend([int(i) for i in alist[0].split(' ')])
            elif type(alist)==type(1):
                self.add(i)
            else:
                self.add(alist[0])
        else:
            for i in alist:
                if type(i)==type(range(1,2)):
                    self.extend(list(i))
                elif type(i)==type(1):self.add(i)
                elif type(i)==type(' '):
                    self.extend([int(j) for j in i.split(' ')])
                else:
                    self.extend(i)
        return None
    def __iter__(self):
        i = 0
        while i<len(self):
            yield self[i]
            i+=1
    def len(self):
        return len(self)
    def add(self, *args):
        if type(args[0])==type([1]):
            if len(args)>1:
                tmp = []
                [tmp.extend(i) for i in args]
                args = tmp
            else:args = args[0]
        if type(args)==type(''):args = [int(i) for i in args.split(' ')] 
        self.extend(args)
        return None
    def index(self,val):
        gen = [i for i,x in enumerate(self) if x == val]
        return gen
    def count(self,n):
        a = self.index(n)
        if type(a)==type(1):return 1
        return len(a)
    def __rmul__(self,other):
        b = type(self[0])
        a = type(other[0])
        if a != b:assert('Both inputs must be of the same type.')
        la = len(self)
        lb = len(other)
        if a==type([]):
            wa = len(self[0])
            wb = len(other[0]) 
            if wa!=lb:assert('inner dimensions must match')
            if not all(len(i)==wa for i in self) and all(len(i)==wb for i in other):
                assert('all rows must be of the same length')
            return self.matmul(self,other,1)
        if a==type(1):
            if la!=lb:assert('inputs must be of the same length.')
            return self.linmul(self,other)
    def __mul__(self,other):
        a = type(self[0])
        b = type(other[0])
        if a != b:assert('Both inputs must be of the same type.')
        la = len(self)
        lb = len(other)
        if a==type([]):
            wa = len(self[0])
            wb = len(other[0]) 
            if wa!=lb:assert('inner dimensions must match')
            if not all(len(i)==wa for i in self) and all(len(i)==wb for i in other):
                assert('all rows must be of the same length')
            return self.matmul(self,other)
        if a==type(1):
            if la!=lb:assert('inputs must be of the same length.')
            return self.linmul(self,other)
    def linmul(self,a,b):
        return [a[i]*b[i] for i in range(len(a))]
    def matmul(self,a,b,i=0):
        from functools import reduce
        if i:b,a=a,b
        r,c = len(a[0]),len(b)
        ret = [[0]*r]*c
        ret = [[1,2],[3,4]]
        for line,ra in enumerate(a):
            for cb in range(c):
                ret[line][cb]=sum(self.linmul([i[cb] for i in b],ra))
        return ret
