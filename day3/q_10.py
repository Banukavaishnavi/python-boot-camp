#print the element in a particular index (cyclic rotation)3 6 8 4 61 2

my_list=list(map(int,input().split(" ")))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])