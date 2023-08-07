#classes and objects
#constructor
class Person:
    def __init__ ( self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def Sayhello(self):
        print("Hello my name is ", self.name)
        print("My age is ", self.age)
        print("My roll no is ", self.rollno)

A=Person("Sowmiya",20,203304)
A.Sayhello()

#example
class Person:
    def __init__ ( self,name):
        self.name=name
        print(self.name)
A=Person("Sowmiya")
A.name

#example 1
#class A:
   # i=123
  #  def __init__ ( self):
 #       self.i=12345
#print(A).i
#print(A().i)

#example 2
#constructor
class Person:
    def __init__ ( self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno
    def Sayhello(self):
        print("Hello my name is ", self.name)
        print("My age is ", self.age)
        print("My roll no is ", self.rollno)

A=Person("Sowmiya",20,203304)
B=Person("Sonashree",21,203020)
C=Person("Pooja",20,203032)
D=Person("Priyadharshini",21,203007)
E=Person("ShreeNila",21,203036)
A.Sayhello()
B.Sayhello()
C.Sayhello()
D.Sayhello()
E.Sayhello()

#example 3
#destructor
class Person:
    def __init__ ( self,name):
        self.name=name
    def Sayhello(self):
        print("Hello my name is ", self.name)
    def __del__(self):
        print("I am ",self.name)
A=Person("Sowmiya")
A.Sayhello()

#Inheritance
class Office:
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isName(self):
        return False
class Name(Office):
    def isName(self):
        return True
A=Office("Sowmiya")
print(A.getName(),A.isName())
A=Office("Sona")
print(A.getName(),A.isName())

