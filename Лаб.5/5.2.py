import random;

list1=[round(random.uniform(-100, 100),1) for i in range(10)]
list2=[round(random.uniform(-100, 100),1) for i in range(10)]

max1=-999999
max2=-999999
print('Исходные массивы:\n',list1,'\n',list2 )

for i in list1:
	if i>max1:
		max1=i

for j in list2:
	if j>max2:
		max2=j

index1=list1.index(max1)
index2=list2.index(max2)

list1[index1],list2[index2]=list2[index2],list1[index1]

print('Массивы, в которых максимальные элементы поменялись местами:\n',list1,'\n',list2)