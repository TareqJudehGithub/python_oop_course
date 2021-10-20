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

Class definition:
 Class definition the actual implementation of a class in a programming language.

- Class has two main parts:  
     - Header 
          - The first line in a class definition.
          - Specifies the name of the class and if it inherits from another 
            class.
          - class header syntax: 
             <keyword> <ClassName>:
             class MyClass:

     - Body
          Contains the elements of the class, including the attributes and the
          behavior of the objects.

    
     class NewClass:          # class header

          # class attributes  # class body
          # __init__() 
          # methods - defines the action that the objects can perform.
          
     - The __init__() method is called automatically when an instance is 
       created to initialize the values of the attributes of the instance.

          - pass keyword is used to fill the body of class/function.
     

"""
print('')
# Backpack class
class Backpack:
     def __init__(self, color, price, weight = 5):
          self.color = color
          self.price = price
          self.weight = weight
     
     def __str__(self):
          return f'Backpack details:\nColor:\
{self.color}\n\
Price: {self.price}\n\
Weight: {self.weight}'


     # def backpack_details(self):
     #      """Backpack details"""
     #      print(f'Backpack details:\nColor: {self.color}\nPrice: {self.price}\nWeight: {self.weight}')


if __name__ == '__main__':
     travel_backpack = Backpack('Black', '$25')
     print(travel_backpack)


