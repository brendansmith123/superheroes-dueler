# dog.py
class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed
    print("dog initialized!")

  def bark(self):
    print("Woof!")

my_dog = Dog("Rex", "SuperDog")
# Remember python implicitly passes in "self",
# so we don't need to pass it in when we call the function!
my_dog.bark()
