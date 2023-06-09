class Bike():
    def __init__(self,inventory):
        self.inventory = inventory
        self.total_income = 0

    def show_inventory(self):
        print("Cecilia's Bike Rental Shop Inventory:")
        return self.inventory

    def hourly_type(self,number,time):
        if number <= 0:
            print("Invalid input")
            return

        if number > self.inventory["hourly"]:
            print ("Sorry, we can't provide that quantity of bikes")
            return

        print("Rented hourly type")
        self.total_income += number * 5 * time
        self.inventory["hourly"] -= number

    def daily_type(self, number, time):
        if number <= 0:
            print("Invalid input")
            return

        if number > self.inventory["daily"]:
            print("Sorry, we can't provide that quantity of bikes")
            return

        print("Rented daily type")
        self.inventory["daily"] -= number
        self.total_income += number * 20 * time

    def weekly_type(self,number, time):
        if number <= 0:
            print("Invalid input")
            return

        if number > self.inventory["weekly"]:
            print("Sorry, we can't provide that quantity of bikes")
            return

        print("Rented weekly type")
        self.inventory["weekly"] -= number
        self.total_income += number * 60 * time

    def rent_Bike(self):

        bikes = int(input("How many bikes would you like to rent?"))
        rent_type= input("What type of rental would you like? (hourly,daily or weekly): ")
        self.rent_type = rent_type
        self.bikes = bikes
        return

    def return_bike(self,rent_type,time,num_bikes):
        bill = 0
        num_bikes=int(input("How many bikes do you want to return?"))
        time= int(input("How many hours, days or weeks did you rent the bikes? "))

        if rent_type =="hourly":
            bill = time * 5 * num_bikes

        elif rent_type == "daily":
            bill = time * 20 * num_bikes

        elif rent_type == "weekly":
            bill = time * 60 * num_bikes

        if (3 <= num_bikes <= 5):
            print("You get Family rental promotion of 30% discount")
            bill = bill * 0.7

        print("Thanks ! Come back soon")
        print("Your total is $", bill)
        return bill

#Creating Objects:
hourly = Bike (200)
daily = Bike (100)
weekly = Bike (70)

# Main Program
while True:
    shop = Bike()
    print("Bike Rental Shop")
    print("1. Display available bikes")
    print("2. Rent a bike")
    print("3. Return a bike")
    print("4. Display shop revenue")
    print("5. Exit")


    choice = input("Enter your choice(1 to 5): ")

    if choice == 1:
            hourly.show_inventory()
            daily.show_inventory()
            weekly.show_inventory()

    elif choice == 2:
            shop.rent_bike()

    elif choice == 3:
            shop.return_bike()

    elif choice == 4:
            shop.total_income()
    elif choice == 5:
           break

    print("Thank you for using our service!")




