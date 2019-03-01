r1=input("enter number of rows in first matrix")
c1=input("enter the number of columns in matrix")
m1=[[None for j in range(c1)] for i in range(r1)]
m2=[[None for j in range(c1)] for i in range(r1)]
for i in range (r1):
    for j in range(c1):
        m1[i][j]=input("enter elements at row"+str(i+1)+"column"+str(j+1))
print "the first matrix is"
for i in range(r1):
    for j in range(c1):
        print m1[i][j],
    print
for i in range(r1):
    for j in  range(c1):
        m2[i][j]=m1[i][j]
    print "the transposed matrix is"
    for i in range (r1):
        for j in range(c1):
            print m2[i][j],
        print
