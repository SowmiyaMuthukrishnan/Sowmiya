#factorial
fact=1
n=7
if n <0:
    print("the factorial doesn't exists in negative")
elif n==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("the factorial of",n,"is",fact)

#reversing a number
n=12345
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of no is",rev)

#palindrome in number
num = 12121
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if(temp == rev):
    print("This value is a palindrome number")
else:
    print("This value is not a palindrome number")

#palindrome in string
string=str(input("Enter a string:"))
rev_str=reversed(string)
if list(string) == list(rev_str):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

#fibonacci
def fibo(n):
    a=0
    b=1
    if(n<0):
        print("Incorrected input")
    elif(n==0):
        return 0
    elif(n==1):
        return b
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b
print(fibo(9))

n=10
num=0
num1=1
nxt_num=num1
count=1
while(count<=n):
    print(nxt_num,end=" ")
    count+=1
    num,num1=num1,nxt_num
    nxt_num=num+num1
print()

#Armstrong number
n=int(input("Enter the number"))
X=len(str(n))
sum=0
temp = n
while temp > 0:
    dig = temp % 10
    sum=sum + dig ** X
    temp = temp // 10
if n == sum :
    print(n , "is an armstrong number")
else:
    print(n, "is not an armstrong number")

