def Euler_31():
    i = 0
    for a in range(0,400,200):
        for b in range(0,300,100):
            x = a+b
            if x>200:break
            for c in range(0,250,50):
                x = a+b+c
                if x>200:break
                for d in range(0,220,20):
                    x = a+b+c+d
                    if x>200:break
                    for e in range(0,210,10):
                        x = a+b+c+d+e
                        if x>200:break
                        for f in range(0,205,5):
                            x = a+b+c+d+e+f
                            if x>200:break
                            for g in range(0,202,2):
                                x = a+b+c+d+e+f+g
                                if x>200:break
                                for h in range(201):
                                    x = a+b+c+d+e+f+g+h
                                    if x==200:i+=1
                                    elif x>200:break
    return i

if __name__=='__main__':
    print(Euler_31())
