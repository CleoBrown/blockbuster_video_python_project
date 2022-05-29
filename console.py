from models.production_company import ProductionCompany
from models.film import Film
from repositories import film_repository, production_company

film_repository.delete_all()
production_company.delete_all()

# ProductionCompanies
anabasis_nv= ProductionCompany('Anabasis NV')
amblin_entertainment =ProductionCompany('Amblin Entertainment')
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
    anabasis_nv,
    amblin_entertainment,
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
"VHS",
20,
1,
2,
twentieth_century_fox),

    Film("Turner & Hooch",
1989,
"Roger Spottiswoode",
"VHS",
10,
3,
4,
touchstone_pictures),

    Film("Raiders of the Lost Ark",
1981,
"Steven Spielberg",
"VHS",
8,
2,
5,
paramount_pictures),

    Film("The Goonies",
1985,
"Richard Donner",
"VHS",
6,
4,
6,
warner_bros),

    Film("Gremlins",
1984,
"Joe Dante",
"VHS",
43,
2,
3,
warner_bros),

    Film("The Karate Kid",
1984,
"John G. Avildsen",
"VHS",
32,
1,
6,
columbia_pictures,),

    Film("A Nightmare on Elm Street", 1984,"Wes Craven",
"VHS",
4,
3,
7,
new_line_cinema),

    Film("Ghostbusters",
1984,
"Ivan Reitman",
"VHS",
65,
2,
4,
columbia_pictures),

    Film("The NeverEnding Story", 1984,"Wolfgang Petersen","VHS", 14,1,5,
constantin_film),

    Film("The Terminator",
1984,
"James Cameron",
"VHS",
32,
2,
3,
cinema_84),

    Film("Weird Science",
1985,
"John Hughes",
"VHS",
16,
3,
8,
universal_pictures), 

    Film("Pet Sematary",
1989,
"Mary Lambert",
"VHS",
21,
2,
9,
paramount_pictures), 

    Film("Friday the 13th",
1980,
"Sean S. Cunningham",
"VHS",
12,
3,
4,
paramount_pictures), 

    Film("The Evil Dead",
1981,
"Sam Raimi",
"VHS",
3,
2,
6,
renaissance_pictures),

    Film("An American Werewolf in London",
1981,
"John Landis",
"VHS",
2,
1,
3,
polygram_pictures),

    Film("Teen Wolf",
1985,
"Rod Daniel",
"VHS",
7,
3,
6,
atlantic_entertainment_group),

    Film("Short Circuit",
1986,
"John Badham",
"VHS",
27,
2,
5,
tristar_pictures),

    Film("Bill & Ted's Excellent Adventure",
1989,
"Stephen Herek",
"VHS",
14,
2,
7,
de_laurentiis_entertainment_group),

    Film("RoboCop",
1987,
"Paul Verhoeven",
"VHS",
5,
2,
2,
orion_pictures),

    Film("The Burbs",
1989,
"Joe Dante",
"VHS",
2,
1,
4,
imagine_entertainment),

    Film("Splash",
1984,
"Ron Howard",
"VHS",
6,
3,
7,
touchstone_pictures),

    Film("Highlander",
1986,
"Russell Mulcahy",
"VHS",
4,
2,
5,
thorn_emi_screen_entertainment),

    Film("Child's Play",
1988,
"Tom Holland",
"VHS",
15,
2,
4,
united_artists),

    Film("Harry and the Hendersons",
1987,
"William Dear",
"VHS",
1,
3,
4,
amblin_entertainment),

    Film("Indiana Jones and the Last Crusade",
1989,
"Steven Spielberg",
"VHS",
8,
2,
5,
paramount_pictures),

    Film("Uncle Buck",
1989,
"John Hughes",
"VHS",
16,
1,
3,
universal_pictures),

    Film("Labyrinth",
1986,
"Jim Henson",
"VHS",
10,
2,
5,
henson_associates),

    Film("E.T. the Extra-Terrestrial",
1982,
"Steven Spielberg",
"VHS",
5,
2,
4,
universal_pictures),

    Film("Aliens",
1986,
"James Cameron",
"VHS",
17,
1,
6,
twentieth_century_fox),

    Film("First Blood",
1982,
"Ted Kotcheff",
"VHS",
3,
2,
5,
anabasis_nv),

    Film("Back to the Future",
1985,
"Robert Zemeckis",
"VHS",
2,
1,
4,
universal_pictures)
    
]

for film in film_list:
    film_repository.save(film)


film_repository.select_all()
