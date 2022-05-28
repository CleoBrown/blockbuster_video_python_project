from flask import render_template, request, redirect
from flask import Blueprint
from repositories import film_repository

blueprint = Blueprint("blockbuster", __name__)

# get products from db
@blueprint.route('/films')
def films():
    films = film_repository.select_all()
    return render_template('films/index.html', films=films)
