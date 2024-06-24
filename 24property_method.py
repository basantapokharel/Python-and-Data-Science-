# class Person:
#     def __init__(self,name,age):
#         self._name=name #protected variable by convention but python donot give error on accessing but not recommended to access it after you see _,also for function
#         self._age=age

#     #getter method
#     def display(self):
#         print(self._name)
#         print(self._age)

#     #setter method
#     def set(self,name,age):
#         self._name=name
#         self._age=age




# person1=Person("Basanta",21)
# print(person1._name)
# print(person1._age)

# person1.display()

#to update 

# person1._name="Mukesh" #works but our convention not doesnt allow it as it is protected variable
# person1.set("Mukesh",25)
# person1.display()


#this task of getter and setter can be done using @property decorator

class Student:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        #getter method for name
        return self._name

    @property
    def age(self):
        #getter method for age
        return self._age
    
    @name.setter
    def name(self,name):
        #setter method for name
        self._name=name

    @age.setter
    def age(self,age):
        #setter method for age
        self._age=age


student1=Student("Basanta",21)
print(student1.name)  #now since we have @property and getter method for name we can access it directly
print(student1.age)

student1.name="Mukesh"
student1.age=25
print(student1.name)
print(student1.age)


