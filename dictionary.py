# to print the information
information={"Name":"Sowmiya",
             "Roll No":203304,
             "Branch":"ECE"}
print(information)

#len
information={"Name":"Sowmiya",
             "Roll No":203304,
             "Branch":"ECE"}
print(len(information))

#access the dictionary  items
information={"Name":"Sowmiya",
             "Roll No":203304,
             "Branch":"ECE"}
print(information["Name"])
print(information["Branch"])

#change the dictionary  items
information={"Name":"Sowmiya",
             "Roll No":203304,
             "Branch":"ECE"}
information["Name"]="Sona"
information["Roll No"]=203020
print(information)

# add items to dictionary
information={"Name":"Sowmiya",
             "Roll No":203304}
information["Branch"]="ECE"
print(information)

# remove items to dictionary
information={"Name":"Sowmiya",
             "Roll No":203304}
del information["Roll No"]
print(information)

#pop and clear
information={"Name":"Sowmiya",
             "Roll No":203304}
information.clear()
print(information)

#update
marks = {'MPMC':97, 'ADC':87}
internal_marks = {'Practical':98}
marks.update(internal_marks)
print(marks)

d = {1: "one", 2: "three"}
d1 = {2: "two"}
d.update(d1)
print(d)
d1 = {3: "three"}
d.update(d1)
print(d)

# Update() when tuple is passed
X = {'x': 2}
X.update([('y', 3), ('z', 0)])
print(X)

# pop an element
sales={'apple':2,'banana':4,'orange':3}
element=sales.pop('apple')
print('the popped element is:',element)
print('the dictionary is:',sales)

#pop not present in dictionary
#sales={'apple':2,'banana':4,'orange':3}
#element=sales.pop('guava')
#print("Element:",element)

sales={'apple':2,'banana':4,'orange':3}
element=sales.pop('guava','banana')
print("Element:",element)

#keys()
x={1:'apple',2:'mango',3:'orange'}
print("Keys:",x.keys())

#update keys
x={1:'apple',2:'mango',3:'orange'}
dict_Keys=x.keys()
print("Before dict updates:",dict_Keys)
x.update({'banana':4})
print("After updates:",dict_Keys)

#values
x={1:'apple',2:'mango',3:'orange'}
print("Values:",x.values())

#values() works when dictionary is modified
sales={'apple':2,'orange':3,'grapes':4}
values=sales.values()
print('Original items:',values)
del[sales['apple']]
print('updated items:',values)

#get()
information={"Name": "Sowmiya",
             "Roll No": 203304,
             "Branch": "ECE"}
dict =information.get("Name")
print(dict)

information={"Name": "Sowmiya",
             "Roll No": 203304,
             "Branch": "ECE"}
print("Getting:",information.get("Roll No"))

person={'Name': 'Sowmiya','age': 20}
print("Name:",person.get('Name'))
print("Age:",person.get('age'))
print("Salary:",person.get('salary'))   # value is not provide
print("Salary:",person.get('salary',0.0)) # value is provide

#person={}
#print("Salary:",person.get('salary'))
#print(person['salary'])

#copy
information={"Name": "Sowmiya",
             "Roll No": 203304,
             "Branch": "ECE"}
information.copy()
print(information)

information={"Name": "Sowmiya",
             "Roll No": 203304,
             "Branch": "ECE"}
age={"Age":20}
information.update(age)
print("After adding the age:",information)
information.copy()
print("Updating the Information:",information)



