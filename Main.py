class Bike:
    def __init__(self,inventory):
        self.inventory = inventory
        self.total_income = 0

    def show_inventory(self):
        print("Cecilia's Bike Rental Shop Inventory:")

    def hourly_type(self,number):
        if number <= 0:
            print("Invalid input")
            return

        if number > self.inventory["hourly_bikes"]:
            print ("Sorry, we can't provide that quantity of bikes")
            return

        print("Rented hourly type")
        self.total_income += number * 5
        self.inventory["hourly bikes"] -= number

    def daily_type(self, number):
        if number <= 0:
            print("Invalid input")
            return

        if number > self.inventory["daily_bikes"]:
            print("Sorry, we can't provide that quantity of bikes")
            return

         print("Rented daily type")
         self.inventory["daily_bikes"] -= number
         self.total_income += number * 20

    def weekly_type(self,number):
        if number <= 0:
            print("Invalid input")
            return

        if number > self.inventory["weekly_bikes"]:
            print("Sorry, we can't provide that quantity of bikes")
            return

        print("Rented weekly type")
        self.inventory["weekly_bikes"] -= number
        self.total_income += number * 60

    def family_rental(self,number):
        if number <= 0:
            print("Invalid input")
            return
        
        if number >= 3 and number <= 5:
        self.total_income +=

#Creating Objects:
hourly_bikes = Bike (200)
daily_bikes = Bike (100)
weekly_bikes = Bike (70)


