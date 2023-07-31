l1=[1,2,3,4]
l2=[2,2,5,6,4]
commen=[]
for i1 in l1:
   
    for i2 in l2:
        if i1==i2 and i1 not in commen:
            commen.append(i1)
print(commen)
            