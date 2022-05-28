from db.run_sql import run_sql

from models.film import Film
from models.production_company import ProductionCompany
from repositories import production_company


def save(film):
    sql = "INSERT INTO films (title, year, director, description, quantity, buying_cost, selling_price, production_company_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    values = [film.title, film.year, film.director, film.description, film.quantity, film.buying_cost, film.selling_price, film.production_company.id]
    run_sql(sql, values)
    id = run_sql("SELECT MAX(id) FROM films")
    film.id = id[0][0]
    return film

def select_all():
    films = []

    sql = "SELECT * FROM films"
    results = run_sql(sql)

    for row in results:
        prod_company = production_company.select(row['production_company_id'])
        film = Film(row['title'], row['year'], row['director'],row['description'],row['quantity'],row['buying_cost'],row['selling_price'],prod_company, row["id"] )
        films.append(film)
    return films   

def select(id):
   
    sql = "SELECT * FROM tasks WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        prod_company = production_company.select(result['production_company_id'])
        film = Film(result['title'], result['year'], result['director'],result['description'],result['quantity'], result['buying_cost'], result['selling_price'], prod_company, result["id"] )
    return film


def update(film):
    sql = "UPDATE films SET (title, year, director, description, quantity, buying_cost, selling_price, production_company_id) = (?, ?, ?, ?, ?, ?, ?, ?) WHERE id = ?"
    values = [film.title, film.year, film.director, film.decription, film.quantity, film.buying_cost, film.selling_price, film.production_company_id, film.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM films"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM films WHERE id = ?"
    values = [id]
    run_sql(sql, values)