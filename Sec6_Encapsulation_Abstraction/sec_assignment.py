 """
 Explain why an attribute is never really private in Python. In your 
 explanation, please explain the process of name mangling with an example.


 An attribute is not really private in Python; because we can access both 
 public and non-public attributes.
 Name mangling is triggered when an attribute name is preceded by two leading
 underscores. 
 Name mangling is only used in a special case where we try to prevent name 
 clashing.
 
 Naming mangling example: 
  class Car:
    def __init__(self, model, year):
      self.model = model
      self.__year = year
  
  # Instantiating object bmw from class Car:
  bmw = Car(model="512", year=2021)

  # accessing year non-public attribute:
  print(bmw._CAR__year)

- Make the following attributes "protected" in the Book class and submit the 
  final version of the class:

      * num_pages
      * ISBN
"""

class Book:
 
	def __init__(self, title, author, num_pages, ISBN, publisher):
		self.title = title
		self.author = author
		self._num_pages = num_pages
		self._ISBN = ISBN
		self.publisher = publisher