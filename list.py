#list in index
x=[1,2,3,4,5]
index=x.index(3)
print(index)

#list in append
languages=["Python","C++","C","Java"]
languages.append("Ruby")
print(languages)
languages.append(32)
print("After Append:",languages)

#list in extend
languages=["Python","C++","C","Java"]
languages.extend("Ruby")
print(languages)
X=[1,3,5]
Y=[2,4,6]
X.extend(Y)
print("List After Extend:",X)

#list in change items
languages=["Python","C++","C","Java"]
languages[3]=("Ruby")
print(languages)

#list in slicing
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']
print(my_list[1:4])
print(my_list[:-7])
print(my_list[7:])
print(my_list[:])
print(my_list[:7])

#list in remove
languages=["Python","C++","C","Java","Swift","R","Rust"]
del languages[3]
print(languages)
del languages[-3]
print(languages)
del languages[0:3]
print(languages)
languages.remove("R")
print("Remove:",languages)

#list in pop
languages=["Python","C++","C","Java","Swift","R","Rust"]
removed_element=languages.pop(5)
print('Removed Elements:',removed_element)
print('Updated List:',languages)
removed_element=languages.pop()
print('Updated List:',languages)
removed_element=languages.pop(-1)
print('Updated List:',languages)

#list in clear
languages=["Python","C++","C","Java","Swift","R","Rust"]
languages.clear()
print('List after clear():',languages)

#list in count
languages=["Python","C++","C","Java","Swift","R","Rust"]
count=languages.count("C++")
print("Count of C++:",count)

#list in sort
languages=["Python","C++","C","Java","Swift","R","Rust"]
languages.sort()
print("Ascending in list:",languages)
languages.sort(reverse= True)
print("Descending in list:",languages)

x=[7,2,3,0,6,4,5,1]
x.sort()
print("Ascending in list:",x)

#list in copy
x=[7,2,3,0,6,4,5,1]
x.sort()
print("Updated list:",x)
y=x.copy()
print("Copied List:",y)

#to add tuple,list&string
x=(1,2,3)+(4,5,6)
print("X=",x)
y=["Python"]+["C++"]
print("Y=",y)

#to create list inside tuple
x=[1,2,3]
y=(4,5,6)
x.extend(y)
print(x)

#list "in" operator to check value inside
languages=["Python","C++","C","Java","Swift","Ruby"]
print("Python" in languages)
print("C++" in languages)
print("CPython" in languages)

#list in iterating
languages=["Python","C++","C","Java","Swift","Ruby"]
for language in languages:
    print(language)

#loop
x=["Sowmiya"]
for my_self in x:
    print(my_self)

#'*' operator
x=["Sowmiya"]*3
for my_self in x:
    print(x)

#swap
x=5
y=4
print("Before swapping the values of x:",x)
print("Before swapping the values of y:",y)
x,y=y,x
print("After swapping the values of x:",x)
print("After swapping the values of y:",y)

#int
x=5/2
print(x)

#adding the int & float value
x=52
y=32.4
z=x+y
print("Z:",z)

x=52
y=32.4
z=x%y
print("Z:",z)

#operators
a = 7
b = 2
# addition
print ('Sum: ', a + b)
# subtraction
print ('Subtraction: ', a - b)
# multiplication
print ('Multiplication: ', a * b)
# division
print ('Division: ', a / b) #Quotient
# floor division
print ('Floor Division: ', a // b) #remainder
# modulo
print ('Modulo: ', a % b) #remainder
# a to the power of b
print ('Power: ', a ** b)

#reverse
x=[7,2,3,0,6,4,5,1]
x.reverse()
print(x)

things=["Pen","Pencil","Notebook"]
things.reverse()
print(things)

