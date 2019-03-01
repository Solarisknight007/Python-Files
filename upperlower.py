#2D MATRIX
sum1=0
sum=0
t=()
r=input("enter the number of rows")
c=input("enter the number of columns")
m=[[None for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        m[i][j]=input("enter value")
t=tuple(m)
for i in range(r):
    for j in range(c):
        print t[i][j], " " ,
    print
for i in range(r):
    for j in range(c):
        if i>j:
            sum=sum+t[i][j]
for i in range(r):
    for j in range(c):
        if (i<j):
            sum1=sum1+t[i][j]
            
print sum1+sum

    


