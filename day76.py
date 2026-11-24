
user=int(input("enter the number"))
new_list=[]
for i in range(1,user):
    if [i-1]+[i-2]==i:
        new_list.append(i)
print(new_list)
    