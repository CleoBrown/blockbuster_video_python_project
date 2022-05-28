from db.run_sql import run_sql
from models.production_company import ProductionCompany
from models.film import Film


def save(production_company):
    sql = "INSERT INTO production_companies (name) VALUES (?)"
    values = [production_company.name]
    run_sql(sql, values)
    id = run_sql("SELECT MAX(id) FROM production_companies")
    production_company.id = id[0][0]
    return production_company

def select_all():
    production_companies= []

    sql = "SELECT * FROM production_companies"
    results = run_sql(sql)

    for row in results:
        production_company = ProductionCompany(row['name'], row["id"])
        production_companies.append(production_company)
    return production_companies


def select(id):
    user = None
    sql = "SELECT * FROM production_companies WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        production_company = ProductionCompany(result['first_name'], result['last_name'], result['id'] )
    return production_company

def update(production_company):
    sql = "UPDATE production_companies SET (name) = (?) WHERE id = ?"
    values = [production_company.name, production_company.id]
    run_sql(sql, values)    


def delete_all():
    sql = "DELETE  FROM production_companies"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM production_companies WHERE id = ?"
    values = [id]
    run_sql(sql, values)