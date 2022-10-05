# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.



class Movie:
    title =""
    director =""
    budget = 0
    def was_expensive(self):
        res = False
        if self.budget>100000000:
         res = True
        return res


Movie1 = Movie()
Movie1.title = "Titanic"
Movie1.director = "James Cameron"
Movie1.budget = 60000000000

Movie2 = Movie()
Movie2.title = "Tadas Blinda"
Movie2.director = "Donatas Ulvydas"
Movie2.budget = 100000


print(Movie1.was_expensive())
print(Movie2.was_expensive())


