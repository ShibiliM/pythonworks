limit=int(input("enter the row"))
for i in range(limit):
    for j in range(limit-i-1):
      
        print(" ",end="")
        for k in range(0,i+1):
            print("*",end="")
       
    print()
