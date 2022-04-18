def factor_count(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    return fc
        
n=int(input())
fc=factor_count(n)
print(fc)
"""
10
1 2 3 4 5 6 7 8 9 10
1+1+    1+        1=4
4
"""
