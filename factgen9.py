def fact(a,b):
            for i in range(a,b+1):
                        fact=1
                        for j in range(1,i+1):
                                    fact=fact*j
                        yield fact
a=input("enter a number")
b=input("enter a number")
for a in fact(a,b+1):
            print a,
                                    
