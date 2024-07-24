#print the unique characters in a given string
#vow="aeiou"
#con="abcdfghjklmnpqrstvwxyz"
ans=" "
i="hello wORLd"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)