#hello-----wor-----ld    --------helloworld
str=input()
count=0
ans=""
for i in str:
    if(i=="-"):
        count+=1
    else:
        ans+=i
print("-"*count+ans)        
                                                     