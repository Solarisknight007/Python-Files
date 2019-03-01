l=[]
n=input("enter no of records")
for i in range(n):
            x=input("enter your list")
            l+=[x]
print "the list you entered is =", l
p=len(l)
for i in range(p):
            for j in range(p-1):
                        if l[j]>l[j+1]:
                                    l[j],l[j+1]=l[j+1],l[j]
print"the sorted list is =",l
                        
