"""
Classes
- They act like “blueprints” that describe the state and behavior of a type of 
  real-world object or concept.
- They are used to represent real-world objects or entities relevant to the 
  context of a program or system. For example, houses, bank accounts, employees, 
  clients, cars, products.

- Main Elements:
- Class Attributes
     __init__()
     Methods

Guidelines:
- Class names are typically nouns. They should start with an uppercase letter. 
  For example: House, Human, Dog, Account.
- If the name has more than one word, each word should be capitalized following 
  the PascalCase naming convention. For example: SavingsAccount.
- The body of the class must be indented.

- Class has two main parts:  
     - Header
          Class definition. Specifies the name of the class and if it inherits
          from another class
     - Body
          Contains the elements of the class, including the attributes and the
          behavior of the objects.

     # class header
     class NewClass:
          # class body
          # class attributes
          # __init__()
          #
          
          - pass keyword is used to fill the body of class/function.
     


"""
print('')
# Backpack class
class Backpack:
     def __init__(self, color, price, weight = 5):
          self.color = color
          self.price = price
          self.weight = weight
          self.backpack_details()

     def backpack_details(self):
          """Backpack details"""
          print(f'Backpack details:\nColor: {self.color}\nPrice: {self.price}\nWeight: {self.weight}')


travel_backpack = Backpack('Black', '$25')


