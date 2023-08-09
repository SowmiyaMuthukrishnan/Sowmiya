#to print the numbers using while loop
i=1
while(i<=10):
    print(i)
    i=i+1

#to print the numbers from 0 to 99
for i in range(100):
    print(i)
#if statement
import math
x=30
if(x<=15):
    y=x+15
elif(x<=30):
    y=x+30
else:
    y=x
print("Y=")
print(math.sin(y))

#while loop inside else
x=2
while(x<3):
    print(x)
    x=x+1
else:
    print("Hello")

#to print the tables
i=1
n=2
while(i<=10):
    print(n,"*",i,"=",n*i)
    i=i+1

#list in while loop
n=[1,2,3,4,5]
i=4
while i<len(n):
    n[0]=n[0]+100
    n[1]=n[1]+100
    n[2]=n[2]+100
    n[3]=n[3]+100
    n[4]=n[4]+100
    i=i+1
    print(n)

