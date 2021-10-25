"""
Name Mangling
 - Name Mangling uses two leading underscores.
 - Name Mangling is only used in special cases to avoid name clashes.
 - Name clashing affects readability and testing.
 - Name Mangling is only meant to be used internal within the class.
 - Name Mangling is not recommended to use, the recommended way is to use a 
   single leading underscore.
 - To call a Name Mangling attribute, we start with the class name of that 
   attribute preceded by a one leading underscore, following by the attribute
   name preceded by a double underscores.
    _Class__<attribute>


"""

class  BackPack:
  def __init__(self):
    self.__items = ["Bread", "Milk"]
  
  def __repr__(self):
    return f"<BackPack(Items: {self._BackPack__items})>"


green_bag = BackPack()

# print(green_bag._BackPack__items)  # calling a name mangling attribute


print(green_bag)