a=0
b=1
n=input("enter total no of terms")
t=3
p=(a,b)
for i in range(0,n+1):
    c=a+b
    p+=(c,)
    a,b=b,c
print p
