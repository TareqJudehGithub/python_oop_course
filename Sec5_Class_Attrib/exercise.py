# Define class attribute

class Quadruped:
    num_feet = 4

    def __init__(self, name, age, specie='Cat'):
        self.name = name
        self.age = age
        self.specie = specie


tom = Quadruped(name='Tom', age=8)
print(tom.name)
print(tom.num_feet)

print('')

spike = Quadruped('Spike', 10, 'Dog')
print(spike.name)
print(spike.num_feet)

print('\n')
print('====================')
print('')


class MyEditorialBook:
    has_cover = True
    editorial_code = 39012

    def __init__(self, title, num_pages, published):
        self.title = title
        self.num_pages = num_pages
        self.published = published


# Add your variables below this line


cover = MyEditorialBook.has_cover
print(cover)

code = MyEditorialBook.editorial_code
print(code)

print('\n')
print('====================')
print('')


# Create a Pizza class, with class attribute price for each type of pizza instantiated


class Pizza:
    price = int()

    def __init__(self, name, topping, crust):
        self.pizza_name = name
        self.topping = topping
        self.crust = crust
        self.pizza_price = Pizza.price

    def pizza_info(self):
        return f'Pizza Info:\n' \
               f'Name: {self.pizza_name}\n' \
               f'Ingredients: {self.topping}\n' \
               f'Style: {self.crust}\n' \
               f'Price: {self.pizza_price}'


margherita = Pizza('Margherita', ['Mozzarella', 'Tomato Sauce'], 'New York')
margherita.pizza_price = '$5'
print(margherita.pizza_price)

salami = Pizza('Salami', ['Salami', 'Mozzarella', 'Tomato Sauce'], 'Chicago')
salami.pizza_price = '$10'
print(salami.pizza_price)

print('')
# calling pizza_info
print(salami.pizza_info())

print('\n')
print('====================')
print('')


class Spider:

    num_legs = 8
    num_eyes = 8

    def __init__(self, name, age, code, species):
        self.name = name
        self.age = age
        self.code = code
        self.species = species


Spider.num_legs = 5
Spider.num_eyes = 6

print(Spider.num_legs, Spider.num_eyes)

print('\n')
print('====================')
print('')

# Assignment: Mini Project | Employees and Class Attributes
