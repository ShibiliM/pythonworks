word=['apple','banana','cherry','date']
comnltr=False
for word1 in word:
    for word2 in word:
        if word1==word2:
            continue
            comnltr=False
        for ltr in word1:
            if ltr in word2:
                # print(ltr)
                comnltr=True
        if comnltr==True:
            print(f"({word1},{word2})")