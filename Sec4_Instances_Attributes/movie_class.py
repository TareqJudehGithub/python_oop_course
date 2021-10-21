class Movie:
  def __init__(self, title, year, rating, language="English"):
    self.title = title
    self.year = year
    self.language = language
    self.rating = rating

  def __str__(self):
    print("\n")
    return f"Title: {self.title}\nYear: {self.year}\nLanguage: {self.language}\n\
Rating: {self.rating}"


if __name__ == "__main__":
  rambo = Movie(title="John Rambo", year=2008, rating=18)
  
  # Modify attribute value
  rambo.rating = 16
  print(rambo)

  Dune = Movie(title="Dune", year=2021, rating=18, language="French")
  print(Dune)


