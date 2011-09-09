# The matrix to check
with open('script/matrix.txt') as f:
    alist = list(x for x in f.read().split('\n'))
blist = list(alist[alist.index(y)].split(',') for y in alist)
clist = []
for z in blist[1:-1]:
    clist.append(list(int(x) for x in z))
print(len(clist))
matrix = clist

# Search through and update - same algorithm as the C code above.
def process():
  col,row,iter,curr,acc = 78,0,0,0,0
  while col >= 0:
    row = 0
    while row < 80:
      iter,curr,acc = row + 1, matrix[row][col+1],0
      while iter < 80 and acc + matrix[iter][col] < curr:
        if acc + matrix[iter][col] + matrix[iter][col + 1] < curr:
          curr = acc + matrix[iter][col] + matrix[iter][col + 1]
        acc += matrix[iter][col]
        iter += 1
      if row > 0 and matrix[row - 1][col] < curr:
        curr = matrix[row - 1][col]
      matrix[row][col] += curr
      row += 1
    col -= 1

# Find the smallest value in the left hand colum.
def themin():
  min = matrix[0][0]
  for row in range(1,80):
    if matrix[row][0] < min:
      min = matrix[row][0]
  return min

# Process the matrix
process()
# Print the least cost.
print (themin())
