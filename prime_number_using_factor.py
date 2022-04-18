def factor_count(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc
        
n=int(input())
fc=factor_count(n)
print(fc)
if fc==2:
    print("prime")
else:
    print("not_a_prime")
"""
13
1 2 3 4 5 6 7 8 9 10 11 12 13
1+1
2 prime
"""
