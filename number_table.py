a,b=map(int,input().split())
n=1
for i in range(1,2*a+1):
    if i<=a:
        print(a,i,i*a)
        i+=1
    else:
        print(a,n,a*n)
        n+=1
        
"""
5 5
5 1 5
5 2 10
5 3 15
5 4 20
5 5 25
5 1 5
5 2 10
5 3 15
5 4 20
5 5 25
"""
