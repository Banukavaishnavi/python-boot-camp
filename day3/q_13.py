# replace the elements in an array with avg of min and max element
my_list=list(map(int,input().split(" ")))
max=my_list[0]
for i in range(len(my_list)): 
    if(my_list[i]>max):
        max=my_list[i]
        print(max)
        my_list=list(map(int,input().split(" ")))
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
        print(min)
avg=(min+max)//2
print(avg)
for i in range(len(my_list)):
    
        
