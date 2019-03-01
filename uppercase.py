phonedict={}
n=input("Enter number of entries: ")
for i in range(n):
    name=raw_input("Enter name: ")
    number=input("Enter phone number: ")
    phonedict[name]=number

print phonedict

def search():

    name=raw_input("Enter name: ")
    for i in phonedict:
            if i==name:
                        print i,phonedict[i]
                        break
            else:
                        print "Name not found"
	
def modify():
            for i in phonedict:
                name=raw_input("Enter name for which number is to be modified: ")
                if name==i:
                    number=input("Enter phone number: ")
                    phonedict[name]=number
                    print "Number has been changed"
                    print "New dictionary",phonedict
                    break
                else:
                        print "Name not found"
        
def add():
            name=raw_input("Enter name: ")
            number=input("Enter phone number: ")
            phonedict[name]=number
            print "Dictionary after adding a entry",phonedict
            def delete():

                        for i in phonedict:
                            name=raw_input("Enter name: ")
                            if name==i:
                                del phonedict[i]
                                break
                        
                            else:
                                print "Name not found"     
                                print "Dictionary after deletion is",phonedict

while True:
	    
            print "------------------------------"
            print "Select your option:"
            print "------------------------------"
            print "1.Search a number"
            print "2.Add a number"
            print "3.Modify a number"
            print "4.Delete a number"
            print "5.Exit"

            ch=input("Enter choice: ")

            if ch==1:
                search()
            elif ch==2:
                add()
            elif ch==3:
                modify()
            elif ch==4:
                        delete()
            elif ch==5:
                        break
            else:
                        print "Invalid choice"
