# Duotas "users" sąrašas.

# Parašykite dvi funkcijas, kurios:
# * Turės 'docstring' tipo komentarą apie tai, ką jos atlieka.
# * Nekeis sąrašo, priimto kaip argumento, savo viduje.
# * Atliks nurodytas užduotis:

# 1. funkcija "filter_all_or_nothing_people" - kaip argumentą priims "users"
# sąrašą ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie arba neturi
# naminių gyvūnų visiškai, arba turi ir šunį, ir katę.

# 2. funkcija "filter_underaged_owners" - kaip argumentą priims "users" sąrašą
# ir duoto sąrašo atveju grąžins sąrašą vartotojų, kurie dar nėra pilnamečiai,
# bet turi bent vieną naminį gyvūną.

users = [
    { 'id': '1', 'name': 'John Smith', 'age': 17, 'hasDog': True, 'hasCat': True },
    { 'id': '2', 'name': 'Ann Smith', 'age': 24, 'hasDog': True, 'hasCat': False },
    { 'id': '3', 'name': 'Tom Jones', 'age': 63, 'hasDog': True, 'hasCat': True },
    { 'id': '4', 'name': 'Rose Peterson', 'age': 20, 'hasDog': True, 'hasCat': False },
    { 'id': '5', 'name': 'Alex John', 'age': 25, 'hasDog': False, 'hasCat': False },
    { 'id': '6', 'name': 'Ronald Jones', 'age': 31, 'hasDog': False, 'hasCat': True },
    { 'id': '7', 'name': 'Elton Smith', 'age': 16, 'hasDog': True, 'hasCat': False },
    { 'id': '8', 'name': 'Simon Peterson', 'age': 32, 'hasDog': False, 'hasCat': True },
    { 'id': '9', 'name': 'Daniel Cane', 'age': 15, 'hasDog': False, 'hasCat': False },
]

# def filter_all_or_nothing_people (users):
#     if users['hasDog' and 'hasCat'] == False:
#         return True
#     else:
#         return False
# new_users = filter(filter_all_or_nothing_people, users)
# for i in new_users:
#     print(dict(i)['name'])

def filter_all_or_nothing_people (users):

   for x in users:
       if (x['hasDog']==True and x['hasCat']==False) or (x['hasDog']==False and x['hasCat']==True):
           users.remove(x)
   return users

def filter_underaged_owners (users):

    for x in users:
        if (x['age']>18) or (x['age']>18 and x['hasDog'==False]):
            users.remove(x)
    return users

print("filter_all_or_nothing_people")
users1 = filter_all_or_nothing_people (users)
for x in users1:
    print(x)
print("filter_underaged_owners")
users2=filter_underaged_owners (users)
for x in users2:
    print(x)















