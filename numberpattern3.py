limit=int(input("enter the row"))
for i in range(1,limit+1):
    for j in range(1,i+1):
        if j%2==0:
            print("2",end=" ")
        else:
            print("1",end=" ")
                         
       
    print()