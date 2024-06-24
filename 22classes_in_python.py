#camelcase is followed for class ie BookName
#snakecase is followed for function name ie book_name

# class Book:
#     pass

# obj=Book()
# print(type(obj))
# print(obj)
# print(Book)


# class Book:
#     #attributes or properties section 
#     #these are class properties
#     # title=""
#     # author=""
#     # price=0.0
#     # discount=0.0
#     class_variable="I am a class variable"

#     def __init__(self,title,author,price,discount):
#         #constructor is used to initialize the properties of the object
#         # print("I am constructor of class Book:",self)
#         self.title=title
#         self.author=author
#         self.price=price
#         self.discount=discount


#     #Behaviour or method sectin 
#     def calculate_sp(self):
#         sp=self.price-(self.price*(self.discount)/100)
#         return sp


# #Instantiating the class or making the object
# book1=Book("Python","Basanta",120,10)
# book2=Book("C++","Hari",100,20)


# #accessing objects properties

# print(book1.author)
# print(book1.price)
# print(book1.discount)
# print(book1.class_variable)
# print(book2.class_variable)

# print(book1.calculate_sp())














#methods 

class student:
    position="std"
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    #instance method(can be called by instance or class but with an object)
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)
        print(self.position)
    
    # @classmethod
    # def display2(cls):
    #     print(cls.position)
        # print(cls.name) #this will give error

    #class method is used to create new object
    # @classmethod
    # def create_object(cls,name,age,marks):
    #     return cls(name,age,marks) #calls the class constructor


    #static method
    #cant access any of the class and object attributes
    @staticmethod
    def display3(a,b):
        print(f"sum:{a+b}")



# s1=student("Basanta",20,90)
# s1.display()
# student.display(s1) ie.
# instance methods can be called by the class itself. However, when calling an instance method from the class, you would typically need to provide an instance of the class as an argument to the method or have a way to access an existing instance within the class.
#instance method can access both class and instance properties


#class method:> can be called by both class and obhect 
#->has access to only class properties(object properties)
#->use decorator and first parameter is cls(for class object)


#class method



#calling class method

# student.display2()

#calling class method to create an object

# s2=student.create_object("Mukesh",40,24)
# print(s2.name)
# print(s2.age)
# print(s2.marks)



#static method
#calling 
#can be called by both class and object
# student.display3(10,20)








