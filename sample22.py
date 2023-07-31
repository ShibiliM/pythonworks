password=input("enter password")
lower=False
upper=False
length=False
digit=False
for i in password:
    if len(i)<8:
        length=True
    if i.isupper():
        upper=True
    if i.islower():
        lower=True
    if i.isdigit():
        digit=True
if lower==True and upper==True and length==True and digit==True:
    print("valid password")
else:
    print("invalid password")