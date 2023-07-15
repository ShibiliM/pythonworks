age=int(input("enter age"))
day=input("enter the day")
if age<=12 or age>=65:
    print("ticket cost is 5")
elif age>12 and age<=18 and day=='wedensday':
    print("ticket cost is 4")
else:
    print("ticket cost is 8")    