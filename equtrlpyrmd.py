height=int(input("enter the no of rows"))
for i in range(height):
    print(" "*(height-i-1),end="")
    print("*"*(2*i+1))
