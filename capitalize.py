name=input("enter a name")
nm= name.split()
new=""
for i in range(len(nm)-1):
    val=nm[i]
    new=new+nm[0].title()+" "

new=new+nm[-1].title()
print(new)
 
  
