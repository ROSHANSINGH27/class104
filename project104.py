import csv
from collections import Counter

with open("D:\project\class104\SOCR-HeightWeight.csv") as f:
    csv_reader=csv.reader(f)
    data=list(csv_reader)

data.pop(0)


Weight=[]

for i in data:    
    Weight.append(float(i[2]))#float is a data type here we are using it to convert the string to number


n=len(Weight)#len is calculating the lenth of Weight and storing it in a varriable n

sum=0
for i in Weight:
    sum=sum+i
mean=sum/n    
print(mean)

Weight.sort()
if n%2==0:
    median1=Weight[n//2]
    median2=Weight[(n//2)-1]
    median=(median1+median2)/2
else:    
    median=Weight[n//2]

print(median)    


count=Counter(Weight)
occ=0
mdid=0
index=0
for i in count.items():
    if i[1]>occ:
        occ=i[1]
        mdid=index
    index=index+1

mode=0  
index=0
for i in count.items():
    if  index==mdid:
        mode=i[0]
        break
    index=index+1
print(mode)    