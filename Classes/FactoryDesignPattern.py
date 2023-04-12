from abc import ABCMeta, abstractstaticmethod

#Creating an interface (as in python you cant delare a 
#interface it is common practice to play I before the class name)
class IPerson(meta=ABCMeta): # meta means you cant create an instance of it

    @abstractstaticmethod
    def person_method():
        #Interface Method
        #each different person will have thier own different person_method
        pass

class Student(IPerson):

    def __init__(self):
        self.name = "Basic student name"

    def person_method(self):# wont work unless the interface's method is overwritten
        print("I am a student")

class Teacher(IPerson):

    def __init__(self):
        self.name = "Basic teacher name"

    def person_method(self):
        print("I am a teacher")

class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1
    
if __name__ == "__main__":
    choice = input("What type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()