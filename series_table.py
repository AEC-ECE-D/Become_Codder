a,b=map(int,input().split())
i=1
for i in range(1,2*b):
    if i<b:
        print(a,i,a*i)
    else:
        print(a,b,b*a)
        b-=1
    i+=1
