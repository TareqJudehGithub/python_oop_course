"""
Instance
 - An object created (instantiated) from the class
 - Instances have attributes belonging to their object.
 - Attributes have UNIQUE values for their own instances (objects).
 - __init__()  defind method to initialize the values of the att of
   of the instance created.
 - self is the first paramater in __init__().
 - self is generic way of referring to the current instance of the class.
 - method in a class is similar to a function
 - 

"""

# Below are examples on how we can define instance attributes
print('House')
# House class
class House:
     def __init__(self, price):    # parameters  
          # attributes
          self.price = price


print('\n')
# define a circle class with proper attributes
class Circle:
     def __init__(self, radius):
         self.radius = radius
         self.color = 'Blue'


my_circle = Circle(5)
# print(my_circle.radius)

print('\n')
print('Rectangle')
# class rectangle
class Rectangle:
     def __init__(self, length, width):

          self.length = length
          self.width = width

          self.rectangle_area()

     def rectangle_area(self):
          print(self.length * self.width)


rectangle_area = Rectangle(10, 4)

print('\n')

print('Movie')
# class movie
class Movie:
     def __init__(self, title, year, language, rating):
          self.title = title
          self.year = year
          self.language = language
          self.rating = rating


# Instantiating an object named fav_movie from class Movie
fav_movie = Movie('The Ice Road', 2021, 'English', 'PG-13')
print(fav_movie.title)
print(fav_movie.year)
print(fav_movie.language)
print(fav_movie.rating)

print('')
fav_movie1 = Movie('The Gladiator', 1997, 'English', '18')
print(fav_movie1.title)
print(fav_movie1.year)
print(fav_movie1.language)
print(fav_movie1.rating)


print('\n')
# Creating instances

# First, create a new class named Backpack
# Back to backpack class
class BackPack:
     def __init__(self):
          self.items = list(['Water bottle', 'Book', 'Pencils'])



# Instantiating a new object (instance) from class Backpack
my_backpack = BackPack()

# output the object place in memory
print(my_backpack)


print('')
# Access items list attribute in class Backpack
print(my_backpack.items)

 


