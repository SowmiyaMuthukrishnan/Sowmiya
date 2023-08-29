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

#Appliances
class Appliances:
    def __init__ (self,home,company,market):
        self.home=home
        self.company=company
        self.market=market
    def display(self):
        print("Home appliance is ",self.home)
        print("Company appliance is ",self.company)
        print("Market appliance is ",self.market)

A=Appliances("Fan","Laptops","CCTVs")
A.display()

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

#example 2
class Person(object):
    def get_name(self,name):
        self.name=name
    def get_details(self):
        return self.name
class Student(Person):
    def fill_details(self,name,branch,year):
        Person.get_name(self,name)
        self.branch=branch
        self.year=year
    def get_details(self):
        print("Name : ",self.name)
        print("Branch : ",self.branch)
        print("Year : ",self.year)
class Teacher(Person):
    def fill_details(self,name,branch):
        Person.get_name(self,name)
        self.branch=branch
    def get_details(self):
        print("Name : ",self.name)
        print("Branch : ",self.branch)

person1=Person()
student1=Student()
teacher1=Teacher()

person1.get_name("Sowmiya")
student1.fill_details("Sowmiya","ECE",2020)
teacher1.fill_details("Sowmiya","ECE")

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())

#Enccapsulation
class A:
    def __init__ (self,private):
        self.__private=private
    def getPrivate(self):
        return self.__private
    def setPrivate(self,private):
        self.__private=private

a1=A(14)
a1.getPrivate()

a1.setPrivate(24)
a1.getPrivate()
print(a1.getPrivate())
print(a1.getPrivate())

#to print the string in uppercase
#class Uppercase(object):
    #def __init__(self,object):

     #   self.object=object
    #def inputStr(self):
   #self.object=input()
  #  def displayStr(self):
 #print(self.object.upper())

#a=Uppercase("python")
#a.inputStr()
#a.displayStr()

#Bank
class BankAccount:
    def __init__(self):
        self.balance=0
        print("Hello Welcome To RBI - Reserve Bank of India")
    def deposit(self):
        amount=float(input("Enter the number to be Deposited : "))
        self.balance=self.balance+amount
        print("Amount to be Deposited : ",amount)
    def withdraw(self):
        amount=float(input("Enter the number to be Withdraw : "))
        self.balance=self.balance-amount
        print("Amount to be Withdraw : ",amount)
    def display(self):
        print("Available balance : ",self.balance)

A=BankAccount()
A.deposit()
A.withdraw()
A.display()


