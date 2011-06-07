def e100(top = 10**12):
    blue = 15
    tot = 21
    while tot <top:
          blue,tot = 3*blue + 2*tot - 2, 4*blue + 3*tot - 3
    return blue

if __name__=='__main__':
    print(e100())
