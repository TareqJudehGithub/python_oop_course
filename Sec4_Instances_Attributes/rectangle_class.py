class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  
  def __repr__(self):
    return "<Rectangle(Length: {}, width: {})>".format(self.length, self.width)


my_rectangle = Rectangle(length=10, width=5)
print(my_rectangle)

