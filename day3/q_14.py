n=10
my_list=list(map(int,input().split(" ")))
totalsum=n*(n+1)//2
sum=0
for i in range(len(my_list)):
    sum=sum+my_list[i]
    print(totalsum-sum)
    

