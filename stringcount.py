str1=input("enter a string")
 

count = {}
 
for i in str1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
 

print("Count :\n "+ str(count))

    


    
 