class Film:

    def __init__(
        self, 
        title,
        year,
        director,
        description,
        quantity,
        buying_cost,
        selling_price,
        production_company,
        id = None):

        self.title = title
        self.year = year
        self.director = director
        self.description = description
        self.quantity = quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.production_company = production_company
        self.id = id
        self.mark_up = float(self.selling_price) - float(self.buying_cost)