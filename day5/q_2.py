#check how many vowels are there in a st
str='a,e,i,o,u'
count=0
inp="worLd"
i=inp.lower()
for i in inp:
    if(i in str):
        count+=1
print(count)
