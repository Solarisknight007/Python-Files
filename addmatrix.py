m3=[]
r1=input("enter rows")
c1=input("enter columns")
r2=input("enter rows")
c2=input("enter columns")
m1=[[None for j in range(r1)]for i in range(c1)]
m2=[[None for j in range(r2)]for i in range(c2)]
for i in range(r1):
    for j in range(c1):
        m1[i][j]=input("enter values")
print m1[i][j]," ",
for i in range(r2):
    for j in range(c2):
        m2[i][j]=input("enter values")
print m2[i][j]," ",
m3=m1[i][j]+m2[i][j]
print m3
