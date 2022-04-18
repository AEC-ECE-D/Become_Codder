n=int(input())
mx=0
c=0
pos=0
while True:
    c+=1
    print(n,end=" ")
    if mx<n:
        mx=n
        pos=c
    if n==1:
        break
    if n%2:
        n=n*3+1
    else:
        n=n//2
print()
print(mx)
print(pos)
