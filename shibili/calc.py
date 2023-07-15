discount=10

purchase=float(input("enter purchase amount"))

if purchase >= 100:
    discount1=float(input(discount*purchase/100))
    print(discount1)
else:
    print("no discount")