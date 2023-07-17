

list1 = [1,1,2,1,3,4,1,2,3,4]
list2=[]

print(list1)

for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)