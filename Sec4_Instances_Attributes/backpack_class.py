class BackPack:
  def __init__(self, color, size):
   
    self.color = color
    self.size = size
    self.items = list()
  
  def __repr__(self):
    return f"<Backpack(Color: {self.color},\n Size {self.size},\n Items: {self.items})>"
  
# Instantiate bag objects
my_backpack = BackPack("red", "medium")
# print(my_backpack)

print(my_backpack)

