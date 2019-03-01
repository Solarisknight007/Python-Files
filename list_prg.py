
#iv) WAP to input details of N books in a library..(ref QP)
def issue(l):
    bno=raw_input("enter book no")
    for i in l:             # using list l to visit list elements
        if i[0]==bno:
            i[4]=i[4]-1
            print "Book issued", "total no of ",i[1],"is",i[4]      #l[1]=bookname,l[4] is total no of books of l[1] type
def returned(l):
    bno=raw_input("enter book no")
    for i in range(len(l)):         # using list index to visit list elements
        if l[i][0]==bno:
            l[i][4]=l[i][4]+1
            print "Book Returned", "total no of ",l[i][1],"is",l[i][4]
def add(l):
    print "Enter following information to add book"
    bno=raw_input("enter book no")
    bname=raw_input("enter book name")
    btype=raw_input("enter book type(novel or subject)")
    cost=float(input("Enter price"))
    no_of_books=input("enter book no")
    l+=[[bno,bname,btype,cost,no_of_books]]

def display(l):
    for i in range(len(l)):
        print "Bno\tBname\tBtype\tcost\ttotal nos"
        print l[i][0],"\t",l[i][1],"\t",l[i][2],"\t",l[i][3],"\t",l[i][4]
        
n=input("Enter number of books")
l=[]
for i in range(n):
    bno=raw_input("enter book no")
    bname=raw_input("enter book name")
    btype=raw_input("enter book type(novel or subject)")
    cost=float(input("Enter price"))
    no_of_books=input("enter book no")
    l+=[[bno,bname,btype,cost,no_of_books]]
#print l
ans="y"
while ans=="Y" or ans=="y":
    print "Select from menu"
    print "1. issue"
    print "2.return"
    print "3.Add"
    print "4.Display"
    ch=input("Enter your choice")
    if ch==1:
        issue(l)
    elif ch==2:
        returned(l)
    elif ch==3:
        add(l)
    elif ch==4:
        display(l)
    else:
        print "invalid option"
        break
    ans=raw_input("Press Y to continue")

#output Question
lst=[100,[22,"Ram","11sciF"],[1,[10,20,30],2,"two-D list"],"output"]
print lst
print lst[0]
print lst[1]
print lst[1][2]         
print lst[1][2][1]          
print lst[2][1]
print lst[2][2]
print lst[2][3]
print lst[2][3][2:10]

