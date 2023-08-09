#type
x="Hello World"
print(type(x))

#index
x="Hello World"
print(x[1])

#Neg index
x="Hello World"
print(x[-4])

#slicing
x="Hello World"
print(x[1:6])
print(x[3:])
print(x[:2])
print(x[:])
print(x[:-6])
print(x[-4:-1])

#string doest'n change the values (immutable)
#name="Sowmiya"
#name[1]="e"
#print(name)

#assign a variable to new string
name="Sowmiya"
name="Nila"
print(name)

#loop
name="Sowmiya"
for getting in name:
    print(getting)

#multiline string
x="""
I am Engineering Student & 
I am Proud of Myself
"""
print(x)

#string operations
#compare two strings
x="Hello World!"
y="I am a student"
z="Hello World!"
print(x==y)
print(y==z)
print(z==x)

#adding a two string
x="Sowmiya."
y="M"
result=x+y
print(result)
print(x+y)

#len
name="Sowmiya"
print(len(name))

#'in' operator
name="Sowmiya"
print('i' in name)
print('t' in name)

#upper Case
name="Sowmiya"
print(name.upper())

name="Sowmiya"
print(name[2].upper())

#lower Case
name="SOWMIYA"
print(name.lower())

name="SOWMIYA"
print(name[4].lower())

#swapcase
name="SoWmIyA"
print(name.swapcase())

#partition
string="I am student"
print(string.partition('am'))
string="I am an Engineer"
print(string.partition('not'))
string= "I am Student of Engineering"
print(string.partition('am'))

#replace
x="base ball"
print(x.replace('base','race'))

#split
string="I am student"
print(string.split())

name='Sowmiya,203304,ECE'
print(name.split(','))
print(name.split(':'))

things="pen,pencil,eraser,note book"
print(things.split(',',2))

#isnumeric
str1='1234'
print(str1.isnumeric())
str2="Python34"
print(str2.isnumeric())

#find
information="I am a Engineering Student"
print(information.find("Engineering"))

#startswith
information="I am a Engineering Student"
print(information.startswith("I"))
print(information.startswith("Engineering"))

x="Sowmiya"
x=x+1
print(x)
