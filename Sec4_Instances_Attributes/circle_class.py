class Circle:
  def __init__(self, radius, color):
    self.radius =radius
    # self.color = "Blue"   # in case all instances have the same initial value.
    self.color = color

  def __str__(self):
    return "Radius: %d, color: %s" % (self.radius, self.color)

my_circle = Circle(5, "Yellow")
print(my_circle)


# Updating my_circle instance attribute values
my_circle = Circle(15, "Black")

print(my_circle)

my_circle.radius = 20
my_circle.color = "Red"


print(my_circle)


