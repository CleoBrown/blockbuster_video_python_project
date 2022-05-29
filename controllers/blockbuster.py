from flask import render_template, request, redirect
from flask import Blueprint
from repositories import film_repository, production_company
from models.film import Film
from models.production_company import ProductionCompany

blueprint = Blueprint("blockbuster", __name__)

# get products from db
@blueprint.route('/films')
def films():
    films = film_repository.select_all()
    return render_template('films/index.html', films=films)

@blueprint.route('/films/<id>/edit', methods = ["GET", "POST"])
def edit(id):
    film = film_repository.select(id)
    production_companies = production_company.select_all()
    return render_template('films/edit.html', film=film, production_companies = production_companies)    

@blueprint.route("/films/<id>", methods=['POST'])
def update_film(id):
    title = request.form['title']
    year = request.form['year']
    director = request.form['director']
    description = request.form['description']
    quantity = request.form['quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form ['selling_price']
    prod_company = production_company.select(request.form['production_company_id'])

    film = Film(title, year, director, description, quantity, buying_cost, selling_price, prod_company,id)
    film_repository.update(film)
    return redirect('/films')

@blueprint.route('/films/<id>/delete')
def delete(id):
    film_repository.delete(id)
    return redirect('/films')   


@blueprint.route("/films/new", methods=['GET'])
def new_film():
    production_companies = production_company.select_all()
    return render_template("films/new.html", production_companies = production_companies)

@blueprint.route("/films/create",  methods=['GET','POST'])
def create_film():
    title = request.form['title']
    year = request.form['year']
    director = request.form['director']
    description = request.form['description']
    quantity = request.form['quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form ['selling_price']
    prod_company = production_company.select(request.form['production_company_id'])
    film = Film(title, year, director, description, quantity, buying_cost, selling_price, prod_company,id)
    film_repository.save(film)
    return redirect('/films')

@blueprint.route("/production_company/new", methods=['GET'])
def new_production_company():
    return render_template("/production_companies/new.html")

@blueprint.route("/production_company/create",  methods=['GET','POST'])
def create_prod_co():
    name = request.form['name']
    prod_company = ProductionCompany(name)
    production_company.save(prod_company)
    return redirect('/production_company/new')


@blueprint.route('/production_companies')
def prod_cos():
    prod_cos = production_company.select_all()
    return render_template('production_companies/index.html', prod_cos=prod_cos)