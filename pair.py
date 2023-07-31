ls=[3,8,12,7,6,10,21,15]
tar=18
pair=[]

for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if ls[i]+ls[j]==tar:
            pair.append((ls[i],ls[j]))
print(pair)



