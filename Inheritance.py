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
  def __init__(self, name):
    self.name = name

class Student(Person):
  def study(self):
    print(self.name, "is studying")

s = Student("broccoli")

print(s.name)
s.study()



class Person:
  def __init__(self, name):
    self.name = name

class Student(Person):

  def __init__(self, name, course):
      self.name = name
      self.course = course


s = Student("broccoli", "Python")

print(s.name)
print(s.course)




class Person:
  def __init__(self, name):
    self.name = name

class Student(Person):

  def __init__(self, name, course):
      super().__init__(name)
      self.course = course


s = Student("broccoli", "Python")

print(s.name)
print(s.course)





class Animal:
  def sound(self):
    print("Animal is making a sound")

class Dog(Animal):
   def sound(self):
    super().sound()
    print("Dog is barking")



d = Dog()
d.sound()




class Animal:
  def eat(self):
    print("Animal is eating")

class Mammal(Animal):
  def walk(self):
    print("Mammal is walking")

class Dog(Mammal):
  def bark(self):
    print("Dog is barking")


d = Dog()

d.eat()
d.walk()
d.bark()


# MULTIPLE INHERITANCE

class Father:
  def skill(self):
    print("programmer")

class Mother:
  def hobbie(self):
    print("Painting")

class Child(Father, Mother):
  pass


c = Child()
c.skill()
c.hobbie()




# MULTIPLE INHERITANCE WITH CONSTRUCTORS


class Father:
  def __init__(self):
    self.father_name = "john"

class Mother:
  def __init__(self):
    self.mother_name = "alice"


class Child(Father, Mother):
  def __init__(self):
      Father.__init__(self)
      Mother.__init__(self)

c = Child()

print(c.father_name)
print(c.mother_name)





## isinstance() function

class Animal:
  def eat(self):
    print("Animal is eating")

class Dog(Animal):
  def bark(self):
    print("Dog is barking")

class Cat():
  def meow(self):
    print("Cat is meowing")

d = Dog()
# Check if d is an instance of Dog
print(isinstance(d, Animal))


# CHECKING SUBCLASSES
print(issubclass(Cat, Animal))
