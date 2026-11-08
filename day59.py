#largest increasing substring with time complexity n
list=[1,2,3,1,2,6,7]
current_count=1
largest_count=1
for i in range(1,len(list)):
    if list[i] > list[i-1]:
        current_count +=1    
    else:
        current_count=1
    if current_count > largest_count:
     largest_count=current_count
print(largest_count)
#largest increasing sub_string 
'''
list=[1,2,3,4,1,2,1,3,4]
largest_count=0
for i in range(len(list)):
    count=0
    largest=float('-inf')
    for j in range(i,len(list)):
        if list[j] > largest:
            largest=list[j]
            count+=1
        else:
            break
    if count > largest_count:
        largest_count=count
print(largest_count)'''

#largest sum of increasing substring
'''list=[10,-1,20,-30,1,2,3,4]
largest_sum=0
for i in range(len(list)):
    sum=0
    largest=0
    for j in range(len(list)):
        if list[j] > largest:
            largest=list[j]
            sum += list[j]
        
    if sum > largest_sum:
        largest_sum=sum
print(largest_sum)'''
#find the largest increasing sub string
'''list=[1,2,3,4,5]
new_list=[]
largest_count=0
for i in range(len(list)):
    count=0
    number=float('-inf')
    substring=[]
    for j in range(i,len(list)):
        if list[j] > number :
            count += 1
            substring.append(list[j])
        else:
            break
    if len(substring) > len(new_list):
        new_list=substring
print(new_list)            
            '''
#largest increasing substring with time complexity n
'''list=[1,2,3,4,1,2,3]
largest_count=1
current_count=1
for i in range(1,len(list)):
    if list[i]>list[i-1]:
        current_count+=1
    else:
        current_count=1  
    if current_count > largest_count:
        largest_count=current_count
print(largest_count)   '''
#Maximum Subarray Sum (Brute Force Approach
'''list=[-100,1,20,-30,1,2,3,4]
largest_sum=float('-inf')
new_list=[]
for i in range(len(list)):
    sum=0
    for j in range(i,len(list)):
            sum+=list[j]
            new_list.append(sum)
            if sum > largest_sum:
             largest_sum=sum
print(max(new_list))'''
#
'''numbers = [-100,1,20,-30,1,2,3,4]

current_sum = numbers[0]
largest_sum = numbers[0]

for i in range(1, len(numbers)):
    current_sum = max(numbers[i], current_sum + numbers[i])
    largest_sum = max(largest_sum, current_sum)

print(largest_sum) '''
        
        