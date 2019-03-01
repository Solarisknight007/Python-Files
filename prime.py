f=10
for i in range(2,51):
    for j in range(2,i):
        if i%j==0:
            f=100
            break
    if f==100:
                print i,
            
