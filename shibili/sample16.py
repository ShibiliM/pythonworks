# set

set1={"banana","apple","orange",10}
print(set1)

set1.add("pappaya")
print(set1)

set1.update('ka','ma')
print(set1)
set4={2,3,4,5,}

set5=set1.update(set4)
print(set5)

set1.remove("banana")
print(set1)

set1.clear()

length=len(set1)
print(length)


# concatinate
set2={0,1,2,3}
set3={4,5,7,8}

set4=set3.union(set2)
print(set4)