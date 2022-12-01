class Pet: # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} year old")

    def speak(self):
        print("I don't know what to say")  

class Dog(Pet): # Child Class
    def speak(self): # inherits the speak() method from 'Pet' and overrides it
        print("Bark")

class Cat(Pet): # Child Class
    def __init__(self, name, age, color):
        super().__init__(name, age)  # Need to call it first as the parent initialiastion may be important 
        # 'super()' references the parent class; '.__init__' is the method to inherit
        # This will 
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} year old and I am {self.color}")

pet = Pet("Mike", 12)
pet.show()
pet.speak()
print("\n")

dog = Dog("Jake", 7)
dog.show() # The child class doesn't have its own show() method so inherits from the parent class 
dog.speak()

cat = Cat("Kenny", 4, "White")
cat.show()
cat.speak()