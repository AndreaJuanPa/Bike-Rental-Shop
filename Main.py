# Creating Parent Class
class Bike:
# Creating Methods:
    def __init__(self,stock):
        self.stock = stock
        self.total_cost = 0

    def show_stock(self):
        print("Cecilia's Bike Shop Inventory:")

    def rent_hourly(self,number):
       self.total_cost += number * 5

    def rent_daily(self, number):
       self.total_cost += number * 20

    def rent_weekly(self,number):
       self.total_cost += number * 60

    def family_rental(self,number):


#Creating Objects:
bikes = Bike(200)
