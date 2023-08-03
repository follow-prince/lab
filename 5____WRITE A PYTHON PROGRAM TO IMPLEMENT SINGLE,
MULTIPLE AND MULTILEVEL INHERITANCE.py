# Single Inheritance
class Vehicle:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start_engine(self):
        print("Starting the engine...")


class Car(Vehicle):
    def __init__(self, color, brand, model):
        super().__init__(color, brand)
        self.model = model

    def drive(self):
        print(f"Driving the {self.color} {self.brand} {self.model}...") 


my_car = Car("red", "Toyota", "Camry")
my_car.start_engine()
my_car.drive()

# Multiple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Mammal(Animal):
    def feed_young_with_milk(self):
        pass


class Canine(Mammal):
    def bark(self):
        print(f"{self.name} is barking...")


class PetDog(Canine, Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def wag_tail(self):
        print(f"{self.name} is wagging its tail...")


my_pet = PetDog("Buddy", "Labrador Retriever")
my_pet.make_sound()
my_pet.feed_young_with_milk()
my_pet.bark()
my_pet.wag_tail()

# Multilevel Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print("Studying...")


class Undergrad(Student):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age, student_id)
        self.major = major

    def party(self):
        print("Partying...")


my_undergrad = Undergrad("Alice", 20, "12345", "Computer Science")
my_undergrad.introduce()
my_undergrad.study()
my_undergrad.party()
