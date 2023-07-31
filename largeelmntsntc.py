str = input("Enter a String:")
words = str.split()
longword = words[0] 
leng = len(words[0])
for index,word in enumerate(words):
    if len(word)> leng:
        leng = len(word)
        longword = word
    else:
        pass

print("Longest word: ",longword)

     
 
   