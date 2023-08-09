#pattern
def X(n):
    if(n==0):
        return
    else:
        X(n-1)
        print("* "*n)
n = 5
X(n)

#using for loop
n = 5
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end=" ")
    print()

#print the numbers
X= 5
for i in range(1, X + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

#reverse the *
n = 5
for i in range(0, n):
    for j in range(0,n-i):
        print("*", end=" ")
    print()

a= 5
for i in range(1,a+ 1):
    print(" " * (a - i) + "*" *i)

a= 5
for i in range(1,a+ 1):
    print(" " * (a - i) + " *" *i)

n=5
for i in range(n):
    for j in range(i):
        print(i, end=' ')
    print('')

X= 5
for i in range(1, X + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

X = 4
b = 0
for i in range(X, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

X = 4
n = X
for i in range(X, 0, -1):
    for j in range(0, i):
        print(n, end=' ')
    print("\r")




