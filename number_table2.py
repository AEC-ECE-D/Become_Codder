n,m=map(int,input().split())
j=1
for i in range(1,2*m+1):
    if m>0:
        print(n,m,m*n)
        m-=1
    else:
        print(n,j,j*n)
        j+=1
        
"""
5 5
5 5 25
5 4 20
5 3 15
5 2 10
5 1 5
5 1 5
5 2 10
5 3 15
5 4 20
5 5 25
"""
