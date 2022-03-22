"""
num=int(input())
for i in range(1,2*num):
    if i<=num:
        print(i,end=" ")
    else:
        num-=1
        print(num,end=" ")
"""
num=int(input())
i=1
while num:
    if i<num:
        print(i,end=" ",num*i)
    else:
        print(num,end=" ",num*i)
        num-=1
    i+=1
