ls=[2,3,4,5,6]
pair=[]
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        num1=ls[i]
        num2=ls[j]
        product=num1*num2
        addition=num1+num2
        if product%2==0 and addition%2!=0:
            print(f"pair :({num1},{num2}),product: {product},sum :{addition}")

