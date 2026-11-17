#addition of 2 by 2 matrix
'''a=[[1,2],
   [3,4]]
b=[[5,6],
   [7,8]]
result=[]
for i in range(2):
    row=[]
    for j in range(2):
        row.append(a[i][j]+b[i][j])
    result.append(row)
print("MATRIX ADDITION : ")
for row in result:
    print(row)'''
#addition of 3 by 3 matrics
'''a=[[1,2,3],
   [2,3,4],
   [3,4,5]]
b=[[1,2,3],
   [2,3,4],
   [3,4,5]]
result=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(a[i][j]+b[i][j])
    result.append(row)
for row in result:
    print(row)'''
#makrs analysis
'''marks=[82,93,90,37,39]
total=sum(marks)
average=total/len(marks)
highest=max(marks)
lowest=min(marks)
passed=0
failed=0
for mark in marks:
    if mark >= 40:
        passed+= 1
    else:
        failed+=1
print("TOTAL MARKS",total)
print("AVERAGE MARKS",average)
print("HIGHEST MARKS",highest)
print("LOWEST MARKS",lowest)
print("NUMBER OF STUDNETS PASSED",passed)
print("NUMBER OF STUDNETS FAILED",failed)
'''
