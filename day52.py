#find the largest number from file
'''
with open("day52.txt", "r") as file:
    text = file.read().split()
    largest=0
    for i in text:
        i=int(i)
        if i > largest:
            largest=i
    print("THE LARGEST NUMBER IS ",largest)'''
#find sum numbers from file:
'''with open("day52.txt","r") as file:
    text=file.read().split()
    total=0
    for i in text:
        i=int(i)
        total += i
print(total)'''
    
         
#count even / count odd /odd  sum/even sum/total numbers:
"""odd_sum=0
count_even=0
count_odd=0
total_numbers=0
even_sum=0
with open("day52.txt","r") as file:
    numbers=file.read().split()
    for i in numbers:
        i=int(i)
        if i % 2 == 0:
            count_even += 1
            even_sum += i
            total_numbers += 1
        else:
            count_odd += 1
            odd_sum += i
            total_numbers +=1
print(f'''
TOTAL NUMBERS :{total_numbers}
ODD_SUM : {odd_sum}
EVEN_SUM : {even_sum}
COUNT_EVEN : {count_even}
COUNT_ODD : {count_odd}
''')
"""
#FREQUENCY CHEKER:
'''count_list=[]
numbe_list=[]
largest=float('-inf')
with open("day52.txt","r") as file:
    numbers=file.read().split()
    for i in numbers:
        count=0
        i=int(i)
        for j in numbers:
            j=int(j)
            if i == j:
                count += 1
        if i not in numbe_list:
            count_list.append(count)
            numbe_list.append(i)
for z in count_list:
    z=int(z)
    if z >  largest:
        largest=z

for x in range(len(count_list)):
    x=int(x)
    if count_list[x] == largest:
        print("THE FIRST LARGEST FREQUENT NUMBER IS ",numbe_list[x])'''
#WORD FREQUENCY CALCULATOR
count_list=[]
words_list=[]

largest=0
total=0
with open("day52.txt","r") as file:
    words=file.read().split()
    print(words)
    
    for i in words:
        count=0
        for j in words:
            if i == j:
                count += 1
        if i not in words_list:
            total=total+1
            count_list.append(count)
            words_list.append(i)
for z in count_list:
    z=int(z)
    if z > largest:
        largest=z
for q in range(len(count_list)):
    if count_list[q]== largest:
     print("THE MOST FREQUENT WORD IS ",words_list[q])
        

print('''====WORD===========FREQUENCY=====''')
for a in range(len(words_list)):
    print(f'''{words_list[a]}: {count_list[a]}''')
print("TOTAL UNIQUE WORD : ",total)

        
    


    
        
    
    
       
          
      
      
          
    