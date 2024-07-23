#find the duplicate number in list
my_list=list(map(int,input().split()))
list=[]
for i in (my_list):
    if(i not in[list]):
       list.append(i)
print(list)
   