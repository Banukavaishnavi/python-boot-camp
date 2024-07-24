#using ascii values sum of given number
str=input()
sum=0
for i in str:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)