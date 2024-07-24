# print all the vowels followed by consonent
str='a,e,i,o,u'
con='bcdfghjklmnpqrstvwxyz'
abc='hello'
ans=" "
for i in abc:
    if(i  in str):
        ans+=i
    if(i in abc):
         ans+=i
print(ans)



