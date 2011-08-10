from memorize import memo
@memo
def a(n):
   if n==1: return 0,1
   S,res=a(n-1)
   S+=(n-1)*res 
   return S,S%n
def e326(n):
   S,ret=a(n)
   return ret
 
def hist326(T,P,M):
   """Compute count of values for Sx=sum 0<=p<x a_n % M"""
   H=[0]*M
   S=0
   T+=1
   reps,rem=T//P,T%P
   for x in range(P):
      n=reps
      if x<rem:
         n+=1
      H[S]+=n
      e=e326(x+1)
      S=(S+e)%M
   return sum(h*(h-1)/2) for h in H)

@memo
def a2(n):
    if n==1:return 1
    else:
        return sum([k*a(k) for k in range(1,n)])%n
def f(N,M):
    count = 0
    for q in range(1,N+1):
        print(q/N,end='\r')
        for p in range(1,q+1):
            if sum([a(i)[1] for i in range(p,q+1)])%M==0:count+=1
    return count
if __name__=='__main__':
    print(f(10,10))
    print(f(10**4,10**3))
