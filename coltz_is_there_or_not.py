def coltz_even(n,target):
    while True:
        if n==target:
            return True
        if n==1:
            return False
        if n%2:
            n=n*3+1
        else:
            return n
n,target=map(int,input().split())
res=coltz_even(n,target)
print(res)
