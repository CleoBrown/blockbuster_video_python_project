from models.production_company import ProductionCompany
from models.film import Film

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

# film_repository.delete_all()
# production_company_repository.delete_all()

# ProductionCompanies
atlantic_entertainment_group = ProductionCompany('Atlantic Entertainment Group')
cinema_84 = ProductionCompany('Cinema 84')
columbia_pictures = ProductionCompany('Columbia Pictures')
constantin_film = ProductionCompany('Constantin Film')
de_laurentiis_entertainment_group = ProductionCompany('De Laurentiis Entertainment Group')
henson_associates = ProductionCompany('Henson Associates')
imagine_entertainment = ProductionCompany('Imagine Entertainment')
new_line_cinema = ProductionCompany('New Line Cinema')
orion_pictures = ProductionCompany('Orion Pictures')
paramount_pictures = ProductionCompany('Paramount Pictures')
polygram_pictures = ProductionCompany('Polygram Pictures')
renaissance_pictures = ProductionCompany('Renaissance Pictures')
thorn_emi_screen_entertainment = ProductionCompany('Thorn EMI Screen Entertainment')
touchstone_pictures = ProductionCompany('Touchstone Pictures')
tristar_pictures = ProductionCompany('TriStar Pictures')
twentieth_century_fox = ProductionCompany('Twentieth Century Fox')
united_artists = ProductionCompany('United Artists')
universal_pictures = ProductionCompany('Universal Pictures')
warner_bros = ProductionCompany('Warner Bros')






film_list = [
    Film("Big",
1988,
"Penny Marshall",
"Video",
20,
1,
2,
"Twentieth Century Fox"),

    Film("Turner & Hooch",
1989,
"Roger Spottiswoode",
"Video",
10,
3,
4,
"Touchstone Pictures"

),
    Film("Raiders of the Lost Ark",
1981,
"Steven Spielberg",
"Video",
8,
2,
5,
"Paramount Pictures"

),
    Film("The Goonies",
1985,
"Richard Donner",
"Video",
6,
4,
6,
"Warner Bros."

),
    Film("Gremlins",
1984,
"Joe Dante",
"Video",
43,
2,
3,
"Warner Bros."

),
    Film("The Karate Kid",
1984,
"John G. Avildsen",
"Video",
32,
1,
6,
"Columbia Pictures",

),
    
]
for film in film_list:
    film_repository.save(film)


# user_repository.select_all()

# task_1 = Task("Plant seeds", user1, 30)
# task_repository.save(task_1)

# task_2 = Task("Go for a run", user1, 30, True)
# task_repository.save(task_2)
