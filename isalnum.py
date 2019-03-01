def num():
            l=[]
            x=input("Enter the number of elements =")
            for i in range(x):
                        p=raw_input("Enter your records =")
                        l+=[p]
            for i in l:
                        if i.isalpha():
                                    print i,"*"
                        elif i.isdigit():
                                    print i*2
                                    
num()

                                    
