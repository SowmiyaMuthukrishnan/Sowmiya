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

