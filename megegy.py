import itertools
szamok=list(range(1,21))
kombok=list(itertools.product(szamok,repeat=2))
kombok=[x for x in kombok if not x[0]==x[1]]
szamok=list(range(21,1,-1))

kombok+=list(itertools.product(szamok,repeat=2))

print(kombok)
counter0=0
counter1=0
counter2=0


for item in kombok:
    if item[0]<item[1]:
        counter0+=1
    elif item[0]>item[1]:
        counter1+=1
    else:
        counter2+=1

print(counter0)
print(counter1)
print(counter2)
