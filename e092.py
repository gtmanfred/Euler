def digs(num):
    res = 0 
    while num > 9:
        res,num = res+(num%10)**2,num//10
    return res+(num**2)


nums = dict.fromkeys(range(1,10**7+1),0)
print(len(nums.keys()))
for i in nums.keys():
    num = int(i)
    if i%100000==0:print(i//100000)
    while num!=89 and num!=1:
        num = digs(num)
    if num ==89:nums[i]=1
print('start')
print(sum([nums.get(x) for x in nums.keys()]))

'''
print('out')

print('start')
count = 0
for i in range(1,10**7+1):
    digits = digs(i)
    if nums[digits]==89:count+=1
print(count)
'''
