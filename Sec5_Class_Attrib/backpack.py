class BackPack:
  max_num_items = 10

  def __init__(self):
    self.items = list()


backpack_1 = BackPack()
backpack_2 = BackPack()

# Access class attribute through the class it self
print(BackPack.max_num_items)

# Access class attribute through an instance
print(backpack_1.max_num_items)
print(backpack_2.max_num_items)

print("\nAfter class attribute modification\n")    
# Modify class attribute value for instance backpack_1
BackPack.max_num_items = 15

print(backpack_1.max_num_items)
print(backpack_2.max_num_items)
print(BackPack.max_num_items)

