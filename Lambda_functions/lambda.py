#lambda function
X = lambda: print("Hello World")
X()

#lambda function with an argument
X = lambda name : print("My name is",name)
X("Sowmiya")

#filter out only even items in given list
my_list = [1,5,7,4,3,6,8]
new_list = list(filter(lambda x : (x%2 == 0) , my_list))
print("List of even number:",new_list)

#filter out only odd items in given list
my_list = [1,5,7,4,3,6,8]
new_list = list(filter(lambda x : (x % 2!= 0) , my_list))
print("List of odd number:",new_list)

#filter the age
ages = [13,53,25,19,17,21,30]
adults = list(filter(lambda ages : ages > 18 , ages))
print(adults)

#to double the given item using map()
my_list = [1,5,7,4,3,6,8]
new_list = list(map(lambda x : (x * 2) , my_list))
print(new_list)

#squaring a given list using map()
my_list = [1,5,7,4,3,6,8]
new_list = list(map(lambda x : (x ** 2) , my_list))
print(new_list)

#reduce
from functools import reduce
my_list = [1,5,7,4,3,6,8]
new_list = reduce(lambda x , y: (x + y) , my_list)
print("sum=",new_list)

#adding the number
X = lambda x : x + 4
print(X(6))

#multiply
X = lambda x : x * 4
print("Multiplication of 6 and 4 is ",X(6))

add = lambda x,y,z : (x+y+z)
print("Sum of the values =",add(4,5,6))

#if else within lambda
min = lambda x , y : x if(x<y) else y
print("the number is:", min(35,74))

result = lambda x : f"{x} is even" if x %2==0 else f"{x} is odd"
print(result(12))
print(result(11))

#uppercase()
animals = ['dog','cat','lion','tiger']
upper_animal=list(map(lambda animals : animals.upper(),animals))
print("the uppercase of animals : ",upper_animal)

#uppercase using slicing function
str1 = 'CopyAssignment'
str2 = lambda str2: str2[:].upper()
print(str2(str1))

# reverse and convert a string to uppercase
str1 = 'CopyAssignment'
str2 = lambda str2: str2[::-1].upper()
print(str2(str1))

#tuple
my_tuple = (1,5,7,4,3,6,8)
new_tuple = reduce(lambda x , y: (x + y) , my_tuple)
print("sum=",new_tuple)

#function inside another function
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

#example 1
my_list=["boy","girl"]
new_list=list(map(lambda my_list:my_list.upper(),my_list))
for i in range(0,len(my_list)):
    print(my_list[i],":",new_list[i])

#example 2
my_list1=["boy"]
list1=list(map(lambda my_list1:my_list1.upper(),my_list1))
my_list2=["girl"]
list2=list(map(lambda my_list2:my_list2.upper(),my_list2))

for i in range(0,len(my_list1)):
    print(my_list1[i],":",list1[i])
    print(my_list2[i],":",list2[i])
