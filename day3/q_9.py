#find the  elements that is  present in (k+n) index k=3,n=2
#input  3 6 8 4 61 2
#output 2
#sample 2
#k=3,n=4
#80 70 54 36 72
#output error  
my_list=list(map(int,input().split(" ")))
n=int(input())
k=int(input())
length=len(my_list)
if(length<k+n):
    print("error")
else:
    for i in range(len(my_list)):
        print(my_list[k+n])
        break