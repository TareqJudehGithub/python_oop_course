class Movie:

  # auto-increment id value
  id_generator = 1

  def __init__(self, title, rating):
    self.id = Movie.id_generator
    self.title = title
    self.rating = rating

    # Unique id for newly created movie instances
    Movie.id_generator += 1

  def __repr__(self):
    print("\n")
    return f"<ID: {self.id}\nMovie(Title: {self.title}\nRating: {self.rating})>"


mov_01 = Movie(title="Rambo", rating=7.5)
mov_02 = Movie(title="Titanic", rating=8.5)

print(mov_01)
print(mov_02)