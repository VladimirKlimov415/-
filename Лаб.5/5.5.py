import random;

n=5;

a =[[1]*n for i in range(n)];

for i in range(5):
	for j in range(5):
		if ((i==1 and j==2) or (i==2 and j==1) or (i==2 and j==3) or (i==3 and j==2)):
			a[i][j]=0;
		
print(a)

