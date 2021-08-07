class Dog:
     def __init__(self, name, age, weight, is_male = True):
          self.name = name
          self.age = age
          self.weight = weight
          self.is_male = is_male


my_dog = Dog(name='yogi'.title(), age=5, weight=15, is_male=True)
print(my_dog.name)

print('\n')

# Assignment: Bacteria and Instances

# 1. Create a Bacteria class
class Bacteria:
     def __init__(self, x, y, shape, structure, environment):
          self.x = x
          self.y = y
          self.shape = shape
          self.structure = structure
          self.environment = environment


# 2. Instantiate 3 instances from Bacteria class
bacteria_1 = Bacteria(50, 60, "Spherical", "Capsule", "Water")
bacteria_2 = Bacteria(50, 260, " Rod-shaped", "Cell wall", "Plants")
bacteria_3 = Bacteria(150, 200, "Spiral", "Plasma membrane", "Animals")

print(bacteria_1.x, bacteria_1.y, bacteria_1.shape, bacteria_1.structure, bacteria_1.environment)


print('\n')
# Assignment: Bakery


class Donut:
     def __init__(self, flavor, toppings, filling, size):
          self.flavor = flavor
          self.toppings = toppings
          self.filling = filling
          self.size = size


class Customer:
	def __init__(self, name, age, address, favorite_dessert):
		self.name = name
		self.age = age
		self.address = address
		self.favorite_dessert = favorite_dessert


class Cake:
	def __init__(self, flavor, price, quality):
		self.flavor = flavor
		self.price = price
		self.quality = quality

