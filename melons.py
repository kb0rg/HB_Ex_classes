"""This file should have our melon-type classes in it."""
class AbstractMelon(object):
    name = ""
    color = "unknown"
    imported = False
    shape = "natural"
    seasons = []

    def get_base_price(self):

        base_price = 5.00
        
        if self.name in ["Casaba", "Ogen"]:
            base_price = base_price + 1.00
        if self.imported == True:
            base_price = base_price * 1.5
        if self.shape != "natural":
            base_price = base_price * 2
        return base_price

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = qty * self.base_price
        if self.name == "Watermelon":
            if qty >= 3:
                price = .75 * price
        if self.name == "Cantaloupe":
            if qty >= 5:
                price = .5 * price
        return price

class Watermelon(AbstractMelon):
#        ('Watermelon', 'green', False, 'natural', ['Fall', 'Summer']),
    name = "Watermelon"
    color = "green"
    imported =  False
    shape = "natural"
    seasons = ['Fall', 'Summer']

    def __init__(self):
        super(Watermelon, self).get_base_price()

    ### fixme: this is not working. trying to make it
    # call get_price on cmd line w/o having to use super() at call....
    def get_price(self, qty):
        super(Watermelon, self).get_price()
        
class Cantaloupe(AbstractMelon):
    #     ('Cantaloupe', 'tan', False, 'natural', ['Spring', 'Summer']),
    name = "Cantaloupe"
    color = "tan"
    imported =  False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def __init__(self):
        super(Cantaloupe, self).get_base_price()

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * self.base_price
        if qty >= 5:
            price = .5 * price        
        return price

class Casaba(AbstractMelon):
#    ('Casaba', 'green', True, 'natural', ['Spring', 'Summer', 'Fall', 'Winter']),
    name = "Casaba"
    color = "green"
    imported =  True
    shape = "natural"
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def __init__(self):
        super(Casaba, self).get_base_price()

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price) 
        return price

class Sharlyn(AbstractMelon):
#   ('Sharlyn', 'tan', True, 'natural', ['Summer']),
    name = "Sharlyn"
    color = "tan"
    imported =  True
    shape = "natural"
    seasons = ['Summer']

    def __init__(self):
        super(Sharlyn, self).get_base_price()

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price) 
        return price


class SantaClaus(AbstractMelon):
   # ('Santa Claus', 'green', True, 'natural', ['Winter', 'Spring']),
    name = "Santa Claus"
    color = "green"
    imported =  True
    shape = "natural"
    seasons = ['Winter', 'Spring']

    def __init__(self):
        super(SantaClaus, self).get_base_price()

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price)
        return price

class Christmas(AbstractMelon):
   # ('Christmas', 'green', False, 'natural', ['Winter']),
    name = "Christmas"
    color = "green"
    imported =  False
    shape = "natural"
    seasons = ['Winter']

    def __init__(self):
        super(Christmas, self).get_base_price()

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * self.base_price
        return price

class HornedMelon(AbstractMelon):
   # ('Horned Melon', 'yellow', True, 'natural', ['Summer']),
    name = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ['Summer']

    def __init__(self):
        super(HornedMelon, self).get_base_price()

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price)
        return price

class Xigua(AbstractMelon):
   # ('Xigua', 'black', True, 'square', ['Summer']),
    name = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ['Summer']

    def __init__(self):
        super(Xigua, self).get_base_price()
    
    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price)
        return price



class Ogen(AbstractMelon):
   # ('Ogen', 'tan', False, 'natural', ['Spring', 'Summer'])
    name = "Ogen"
    color = "tan"
    imported =  False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def __init__(self):
        super(Ogen, self).get_base_price()

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * self.base_price
        return price
