class A(exceptions):
            pass
a1=A(" Less then 18")
a2=A("more than 75")
try:
            n=input("enter a age")
            if n<18:
                        raise a1
            elif n>75:
                        raise a2
            else:
                        print"elegible to work"
except A,e:
            print e.message
