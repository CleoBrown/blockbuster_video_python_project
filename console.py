from models.production_company import ProductionCompany
from models.film import Film
from repositories import film_repository, production_company

film_repository.delete_all()
production_company.delete_all()

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


list_prod_cos = [
    atlantic_entertainment_group,
    cinema_84,
    columbia_pictures,
    constantin_film,
    de_laurentiis_entertainment_group,
    henson_associates,
    imagine_entertainment,
    new_line_cinema,
    orion_pictures,
    paramount_pictures,
    polygram_pictures,
    renaissance_pictures,
    thorn_emi_screen_entertainment,
    touchstone_pictures,
    tristar_pictures,
    twentieth_century_fox,
    united_artists,
    universal_pictures,
    warner_bros
]

for prod_co in list_prod_cos:
    production_company.save(prod_co)

film_list = [
    Film("Big",
1988,
"Penny Marshall",
"Video",
20,
1,
2,
twentieth_century_fox),

    Film("Turner & Hooch",
1989,
"Roger Spottiswoode",
"Video",
10,
3,
4,
touchstone_pictures

),
    Film("Raiders of the Lost Ark",
1981,
"Steven Spielberg",
"Video",
8,
2,
5,
paramount_pictures

),
    Film("The Goonies",
1985,
"Richard Donner",
"Video",
6,
4,
6,
warner_bros

),
    Film("Gremlins",
1984,
"Joe Dante",
"Video",
43,
2,
3,
warner_bros

),
    Film("The Karate Kid",
1984,
"John G. Avildsen",
"Video",
32,
1,
6,
columbia_pictures,

),
    
]
for film in film_list:
    film_repository.save(film)


film_repository.select_all()
