from script.sumset import issumset
def e105(f = 'script/sets.txt'):
    count = 0
    with open(f) as f:
        f = f.read().split('\n')[1:-1]
    for i in f:
        line = [int(j) for j in i.split(',')]
        line.sort()
        if issumset(line):
            count+=sum(line)
    return count
if __name__=='__main__':
    print(e105())
