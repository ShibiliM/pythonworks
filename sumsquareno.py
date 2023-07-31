num = int(input("Enter a Number:"))

temp = num
sum = 0
str1=str(num)
for i in str1:
    digit =temp%10
    sum += digit **2
    temp = temp//10
print(sum)