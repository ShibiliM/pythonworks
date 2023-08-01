limit=int(input("enter the row"))
no=1
for i in range(1,limit+1):
    for j in range(1,i+1):
        print(no,end=" ")
        no+=1
    print()
