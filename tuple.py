languages=("hello",)
print(type(languages))

new_tuple=(1,2,3,4,5)
print(new_tuple)

# tuple in index
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[0])
print(letters[5])

# tuple in Neg index
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[-1])
print(letters[-5])

# tuple in slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])
print(my_tuple[:7])

#list to tuple
x=[1,2,3,4,5]
x=tuple(x)
print(x)

#tuple to list
x=(1,2,3,4,5)
x=list(x)
print(x)

# tuple in count
x= ('a', 'p', 'p', 'l', 'e',)
print(x.count('p'))
print(x.count('a'))

#tuple in iterating
languages=("Python","C++","C","Java","Swift","Ruby")
for language in languages:
    print(language)

#tuple "in" operator to check value inside
languages=("Python","C++","C","Java","Swift","Ruby")
print("Python" in languages)
print("C++" in languages)
print("CPython" in languages)

#print in tuple and assign to new tuple
x=(1,2,3,4,5,6)
print(x[:])
my_tuple=x[:]
print("y=",my_tuple)

#'*' operator
x=("Sowmiya")*3
for my_self in x:
    print(my_self)

#loop
x=("Sowmiya")
for my_self in x:
    print(my_self)

