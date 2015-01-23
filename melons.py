"""This file should have our melon-type classes in it."""
class Watermelon(object):
#        ('Watermelon', 'green', False, 'natural', ['Fall', 'Summer']),
    name = "Watermelon"
    color = "green"
    imported =  False
    shape = "natural"
    seasons = ['Fall', 'Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """
        price = qty * self.base_price
        if qty >= 3:
            price = .75 * price
        return price
        
class Cantaloupe(object):
    #     ('Cantaloupe', 'tan', False, 'natural', ['Spring', 'Summer']),
    name = "Cantaloupe"
    color = "tan"
    imported =  False
    shape = "natural"
    seasons = ['Spring', 'Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * self.base_price
        if qty >= 5:
            price = .5 * price        
        return price

class Casaba(object):
#    ('Casaba', 'green', True, 'natural', ['Spring', 'Summer', 'Fall', 'Winter']),
    name = "Casaba"
    color = "green"
    imported =  True
    shape = "natural"
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    base_price = 6.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price) 
        return price

class Sharlyn(object):
#   ('Sharlyn', 'tan', True, 'natural', ['Summer']),
    name = "Sharlyn"
    color = "tan"
    imported =  True
    shape = "natural"
    seasons = ['Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price) 
        return price


class SantaClaus(object):
   # ('Santa Claus', 'green', True, 'natural', ['Winter', 'Spring']),
    name = "Santa Claus"
    color = "green"
    imported =  True
    shape = "natural"
    seasons = ['Winter', 'Spring']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price)
        return price

class Christmas(object):
   # ('Christmas', 'green', False, 'natural', ['Winter']),
    name = "Christmas"
    color = "green"
    imported =  False
    shape = "natural"
    seasons = ['Winter']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * self.base_price
        return price

class HornedMelon(object):
   # ('Horned Melon', 'yellow', True, 'natural', ['Summer']),
    name = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ['Summer']
    base_price = 5.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price)
        return price

class Xigua(object):
   # ('Xigua', 'black', True, 'square', ['Summer']),
    name = "Xigua"
    color = "black"
    imported =  True
    shape = "square"
    seasons = ['Summer']
    base_price = 10.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * (1.5 * self.base_price)
        return price



class Ogen(object):
   # ('Ogen', 'tan', False, 'natural', ['Spring', 'Summer'])
    name = "Ogen"
    color = "tan"
    imported =  False
    shape = "natural"
    seasons = ['Spring', 'Summer']
    base_price = 6.00

    def get_price(self, qty):
        """Determine price for this quantity of melons of this type.
        Return a float of the total price.
        """

        price = qty * self.base_price
        return price


# general formula to use to generate each unique method
# if self.imported == True:
#     price = price * 1.5
# if self.shape != "natural":
#     price = price * 2
# if self.name == "Casaba" or if self.name == "Ogen"
#     price = base_price + (1*qty)

# code review by Katie OK
