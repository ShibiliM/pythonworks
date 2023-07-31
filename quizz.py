uname=input("enter user name")
add=30
sub=10
div=3
mul=6
eligible=18
mark=0

add1=int(input("enter 10 +20=?"))
sub1=int(input("enter 30-20=?"))
div1=int(input("enter 9/3=?"))
mul1=int(input("enter 2*3=?"))
elig=int(input("your age =="))

if uname=="1234":
    if add1==add:
        print("right")
        mark=mark+1
    else:
        print("wrong")
    if sub1==sub:
        print("right")
        mark=mark+1
    else:
        print("wrong")
    if mul1==mul:
        print("right")
        mark=mark+1
    else:
        print("wrong")
    if elig==eligible:
        print("right")
        mark=mark+1
    else:
        print("wrong")
    print(mark)



