from flask import render_template, request, redirect
from flask import Blueprint

blueprint = Blueprint("blockbuster", __name__)


@blueprint.route('/films')
def films():
    # TODO
    # get products from db
    # products = ...
    films = ['movie1', 'movie2', 'movie3']
    # pass to render template
    return render_template('products/films.html', films=films)
