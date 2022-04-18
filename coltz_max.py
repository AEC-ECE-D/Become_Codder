n=int(input())
mx=0
while True:
    print(n,end=" ")
    if mx<n:
        mx=n
    if n==1:
        break
    if n%2:
        n=n*3+1
    else:
        n=n//2
print()
print(mx)

