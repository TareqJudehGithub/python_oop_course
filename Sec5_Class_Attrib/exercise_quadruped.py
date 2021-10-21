class Quadruped:
  num_feet = 4

  def __init__(self, name, age, specie):
    self.name = name
    self.age = age
    self.specie = specie

# access class attributes
print(Quadruped.num_feet)