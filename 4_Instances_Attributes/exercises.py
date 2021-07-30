class Dog:
     def __init__(self, name, age, weight, is_male = True):
          self.name = name
          self.age = age
          self.weight = weight
          self.is_male = is_male


my_dog = Dog(name='yogi'.title(), age=5, weight=15, is_male=True)
print(my_dog.name)