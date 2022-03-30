m,n=map(int,input().split())
for i in range(1,2*m+1):
    if i<=m:
        print(m,n,n*m)
        n-=1
    else:
        i=(2*m-i+1)
        print(m,i,i*m)
