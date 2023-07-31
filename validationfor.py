# password validation

password=input("enter password")
lower=False
upper=False
length=False
digit=False
lengg=len(password)
for i in password:
    # length check
    if lengg>=8:
        length=True

    # uppercase check
    if i.isupper():
        upper=True

        # lowercase check
    if i.islower():
        lower=True

    # digitchech
    if i.isdigit():
        digit=True
if lower==True and upper==True and length==True and digit==True:
    print("valid password")
else:
    print("invalid password")