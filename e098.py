f = open('words.txt').read().split(',')
fset = [set(i) for i in f]
fdict = {f[i]:[fset[i],{j:f[i].count(j) for j in fset[i]}] for i in range(len(f))}
numlist = [i for i in range(1,int(987654322**.5))]
sqrdict = {i**2:i for i in numlist}
print('start')
def e98():
    count = 0
    fd = fdict
    analist = []
    for i in fd.keys():
        if fd.get(i)[0]=='done':continue
        testlist = []
        for j in fd.keys():
            if i == j:continue
            if not fd.get(i)[0].issubset(fd.get(j)[0]):continue
            if not fd.get(j)[0].issubset(fd.get(i)[0]):continue
            test = True
            for k in fd.get(i)[1].keys():
                if not fd.get(i)[1].get(k)==fd.get(j)[1].get(k):test = False
            if test:        #print([i+':',fd.get(i),j+':',fd.get(j)]);count+=1;
                testlist+=[[j]+fd.get(j)]
                fd[j] = ['done']+fd.get(j)
        if testlist:
            analist+=[[[i]+fd.get(i)]+testlist]
    maxret = 0
    print('start solve')
    for i in analist:
        print(i)
        t = [j[0] for j in i]
        ans = solve(t)
        if ans:
            ans = [int(j) for j in ans]
            print(ans)
            if max(ans)>maxret:maxret = max(ans)
    return maxret


import re
import itertools

def solve(puzzle):
    print(puzzle)
    word = re.findall('[A-Z]+', puzzle[0].upper())
    unique_characters = set(''.join(word))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {w[0] for w in word}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        test = []
        if zero not in guess[:n]:
            equation = []
            for i in puzzle:
                equation += [i.translate(dict(zip(characters, guess)))]
            if '1296' in equation:print()
            for i in equation:
                t = int(i)
                if str(t)!=i:break
                if sqrdict.get(t):test+=[i]
                else:break
            if len(test)==len(equation):return test
    return []
if __name__=='__main__':
    print(e98())
