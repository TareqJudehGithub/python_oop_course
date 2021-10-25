class Movie:
  id_generator = 1

  def __init__(self, title, rating):
    self._id = Movie.id_generator     # _id attribute is non-public
    self.title = title
    self.rating = rating

    Movie.id_generator += 1