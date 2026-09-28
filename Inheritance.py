class Animal:
  def eat(self):
    print("Animal is eating")

class Dog(Animal):
  def bark(self):
    print("Dog is barking")

class Cat(Dog):
  def meow(self):
    print("Cat is meowing")


c= Cat()

c.eat()
c.meow()
c.bark()



class Person:
  def __init__(self):
    self.name = "broccoli"
    self.age = 20

class Student(Person):
  pass

s = Student()

print(s.name)
print(s.age)
