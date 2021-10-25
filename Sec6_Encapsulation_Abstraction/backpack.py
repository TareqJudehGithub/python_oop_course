class BackPack:
  def __init__(self, color):
    self.color = color
    self._items = list()    # _items attribute is non-public
  
red_bag = BackPack(color="red")