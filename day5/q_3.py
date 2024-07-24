#write a program to print all the consonents
c=0
count=0
str='a,e,i,o,u'
abc='hello'
for i in abc:
    if(i not in str):
        c+=1
    if(i in str):
         count+=1
print(count)
print(c)


