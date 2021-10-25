"""
Public vs Non-Public Attributes

 - In Python, attributes can be public and non-public.
 - A public attribute can be accessed and modified directly without any access
   restrictions.
 - A non-public attribute is an attribute that shouldn't be accessed nor 
   modified outside the class.
 - In Python, we have two ways of defining a non-public attributes:
    - By naming convection. preceding an attribute name with an _ 
      _<attribute_name>  which will let other developers know that this 
      attribute is non-public, so that attribute shouldn't be accessed or 
      modified outside the class.
    - By Name Mangling mechanism. Activating a mechanism that changes the 
      attribute name and makes it more difficult to access. We can start the
      attribute name by a double leading underscores __<attribute_name>.
"""



# Example of public attributes and non-public attributes

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self._year = year   # non-public attribute
  
  def __repr__(self):
    return f"<Car(Brand: {self.brand}, Model: {self.model}, Year: {self._year})>"
  

car_1 = Car("Porsche", "911 Carrera", 2021)

# We can have access to access and even modify instance attributes (public):
car_1.model = "911"

# access to non-public attribute
print(car_1._year)



