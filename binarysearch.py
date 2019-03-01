a=[]
n=input('enter total number of elements in the list')
for i in range(n):
    x=input("enter elements")
    a+=[x]
print a
k=input("enter value to be found")
y=10
f=0
l=n-1
while f<=1:
    m=(f+1)/2
    if a[m]==k:
        y=100
        break
    elif a[m]<k:
        f=m+1
    else:
        l=m-1
if y==100:
    print "found at",m
else:
    print"not found"
