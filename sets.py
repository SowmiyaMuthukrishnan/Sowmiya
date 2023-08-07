#int type
Numbers={2,3,6,7,5,4}
print("NUMBERS:",Numbers)
#string type
Names={'Sowmiya','Sona','Nila','Pooja','Priya'}
print("NAMES:",Names)
vowels={'a','e','i','o','u'}
print("Vowels:",vowels)
#mixed sets
mixed_values={'Sowmiya','Ece',20,47}
print("Values:",mixed_values)

#empty set
x=set()
print("empty_set:",type(x))

#adding a set
x={23,34,56,78}
print("Given element:",x)
x.add(90)
print("Updates elements:",x)

#update
Names={'Sowmiya','Sona','Nila'}
values=['Pooja','Priya']
Names.update(values)
print(Names)
x={23,34,56,78}
x.update(90)
print("Updated Elements:",x)

#remove
Names={'Sowmiya','Sona','Nila','Pooja','Priya','World'}
print("Given Names:",Names)
names=Names.discard('World')
print("After removed:",Names)

#loop
Names={'Sowmiya','Sona','Nila','Pooja','Priya'}
for name in Names:
    print(name)

#len
Names={'Sowmiya','Sona','Nila','Pooja','Priya','World'}
print(len(Names))


