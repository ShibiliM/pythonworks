num = int(input("Enter a Number:"))

temp = num
sum = 0
str1=str(num)
for i in str1:
    digit =temp%10
    sum += digit **3
    temp = temp//10
if(sum==num):
    print("",num,"is an Armstrong number")
else:
    print("",num,"is not an Armstrong number")
