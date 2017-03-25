x=float(input())
y=float(input())

n=0
while x<=y:
    x=x+0.1*x
    n+=1;
    x+=1;
print (n)