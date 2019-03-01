def factorial(q,p):
            for i in range(q,p+1):
                        fact=1
                        for j in range(1,i+1):
                                    fact=fact*j
                        yield fact,
q=input("enter no")
p=input("enter number")
for a in factorial(q,p+1):
            print a,
