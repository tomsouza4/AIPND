### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28

### TODO: Declare the Pants Class
class Pants(object):
### TODO: write an __init__ function to initialize the attributes
    def __init__(self, color_pnts, waist_size_pnts, length_pnts, price_pnts):
        self.color = color_pnts
        self.waist_size = waist_size_pnts
        self.length = length_pnts
        self.price = price_pnts

### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None
    def change_price(self, new_price):
        self.price = new_price

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount.
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price
    def discount(self, discnt):
        return self.price * (1 - discnt)
