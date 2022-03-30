def mul(x,y):
    sum=0
    while x:
        if x%2:
            sum+=y
        x=x//2
        y=y*2
    return sum
x,y=map(int,input().split())
print(mul(x,y))
        
