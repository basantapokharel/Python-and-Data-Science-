class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_person(self):
        print(self.name)
        print(self.age)

    def person_method(self):
        print("person method")


class Student(Person):
    def __init__(self,name,age,marks,university):
        super().__init__(name,age)    # or with parent name and child as self Person.__init__(self,name,age) both works
        self.marks=marks
        self.university=university

    def display_student(self):
        super().display_person()
        print(self.marks)
        print(self.university)

    def student_method(self):
        print("student method")


#making objects of sub class

student1=Student("Basanta",21,90,"IIT")
student1.display_person()

student1.display_student()
#If name of both display is same method overrides occur to only run subclass's method we explicitly call parents display in method of child method display

student1.person_method()
student1.student_method()
