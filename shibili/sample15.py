# touple

t1=("apple",)
t2=("orange","grape","banana")
print(t1)
print(t2)

t3=t1+t2
print(t3)

p=list(t2)
p.append("pappaya")
j=tuple(p)
print(j)
print(t2)


cot=(t2.count("grape"))
print(cot)
l=(len(t2))
print(l)