def Euler_62():
    cubes = {}
    count = 1
    target = 5

    while True:
        index = ''.join(sorted(str(count**3)))
        if index in cubes:
            cubes[index].append(count)
            if len(cubes[index]) >= target:
                ret=sorted(cubes[index])[0]
                return ret**3
        else:
            cubes[index] = [count]
        count+=1

if __name__=='__main__':
   print(Euler_62())
