# str1=input("enter a string")
# spcchrctr=['@','#','$','*','&']
# str2=str1
# for i in spcchrctr:
    
#     str2=str2.replace(i,"")
# print("original string ",str1)
# print("remove special charecter ",str2)



str1=input("enter a string")
str2=str1
spclchr=['@','#','$','&']


for i in str1:
    if i not in spclchr:
        print(i)

