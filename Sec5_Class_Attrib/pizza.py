class Pizza:
  
  price = 12.99

  def __init__(self, desc, toppings, crust):
    self.desc = desc
    self.toppings = toppings
    self.crust = crust

  def __repr__(self):
    return f"<Pizza(Description: {self.desc}\nTopping: {self.toppings}\n\
Crust: {self.crust})>"


veggie_pizza = Pizza(desc="Mushroom", toppings=["Mushroom, Sauce, Mozzarella"], \
  crust= "New York Style")

print(Pizza.price)

# Update class price attribute
Pizza.price = 13.99

print(Pizza.price)

print(veggie_pizza)