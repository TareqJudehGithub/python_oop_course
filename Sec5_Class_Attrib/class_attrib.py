"""
Class Attribute
 - Class attribute belong to the class.
 - Class attribute does not include self parameter; because class attribute 
   belongs to the class, while self belongs to the instance created from the 
   class.
 - All instances share the class attributes.
 - All instances of the class have access to that class attributes.
 - Class attribute are shared for all instances. So changing their value affects 
   all instances since they all take the value from the same source.
 - There is only one copy of each class attribute.
 - Class attributes Are written before (above) __init__ dunder method.

"""

print('\n')
print('====================')
print('')

print('class Dog')
print('')
# dog class
class Dog:

    species = 'Canius Lupus'

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


spike = Dog('Spike', 5, 'Bulldog')
scooby = Dog('Scooby', 7, 'Lab')


# As we can see, class attribute is shared between all instances.
print(spike.species)
print(scooby.species)


print('\n')
print('====================')
print('')

# backpack class
print('class Backpack')
print('')


class Backpack:

    max_num_items = 10

    def __init__(self):
        self.items = []


backpack_001 = Backpack()
backpack_002 = Backpack()

# accessing a class attribute

 # using instance name
print(backpack_001.max_num_items)
print(backpack_002.max_num_items)

 # or using the class name it self:
print(Backpack.max_num_items)



print('\n')
print('====================')
print('')


# Using class attributes inside and outside the class
print('class Movies')
print('')

class Movies:

    id_counter = 1

    def __init__(self, title, rating):
        # We can call a class attribute, by the class name, or using self keyword:
        self.id = Movies.id_counter
        self.mov_id = self.id_counter
        self.title = title
        self.rating = rating

        # update class attribute value incrementing it by 1, each time we create an instance.
        Movies.id_counter += 1


movie_001 = Movies('Jaws', 8.2)
print(movie_001.id)
# >>> 1


movie_002 = Movies('The Ice Road', 6.3)
print(movie_002.mov_id)
# >>> 2


print('\n')
print('====================')
print('')

# Changing/update class attribute value


class Circle:

    radius = 5

    def __init__(self, color):
        self.color = color
        self.circle_radius = Circle.radius


circle_001 = Circle('Blue')
circle_002 = Circle('Green')


# modify instance circle_001 radius value
circle_001.radius = 10
print(circle_001.radius)

print('')

# As we can see, circle_002 radius value is still the same
print(circle_002.radius)
print(circle_002.circle_radius)



