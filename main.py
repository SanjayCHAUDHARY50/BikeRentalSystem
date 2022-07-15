from BikeRent import BikeRentalCompany
from Customers import Customer

def main():
    rental = BikeRentalCompany(500)
    customer = Customer()
    
    customer.delete_database()
    
    while True:
        print("Welcome To Rental Bike Company \n Choose The Preferred options: \n 1. Check for availability of bikes \n 2. Bikes For Rent \n 3. Customer Data \n 4. Exit")
        
        choose = input("Enter your Option no : ")
        try:
            choose = int(choose)
        except ValueError:
            print("Enter the correct value")
            continue
        
        if choose == 1:
            rental.available()
            
            
        elif choose == 2:
            customer.name = input("Enter Your name : ")
            customer.options = input("Enter the options for bike rent: \n 1. Hourly services(10 per hour) \n 2. Daily services(100 per day) \n 3. Weekly services(500 per week) \n Enter your Options no. : ")
            try:
                customer.options = int(customer.options)
                if customer.options == 1 or customer.options == 2 or customer.options == 3:
                    pass
                else:
                    print("Enter the correct Value... ")
                    break
            except ValueError:
                print("Enter the correct value")
                break
            customer.bikes = input("Enter the total bikes for rent : ")
            try:
                customer.bikes = int(customer.bikes)
            except ValueError:
                print("Enter the correct value")
                break
            if customer.options == 1:
                customer.total_bill = rental.hour_options(customer.bikes)
            elif customer.options == 2:
                customer.total_bill = rental.daily_options(customer.bikes)
            else:
                customer.total_bill = rental.week_options(customer.bikes)
            if customer.total_bill:
                customer.database(customer.name, customer.options, customer.bikes, customer.total_bill)
            else:
                break
            
        elif choose == 3:
            customer.get_details()
        elif choose == 4:
            print("Thank You for Using our Platform")
            break
        else:
            print("Wrong Input, Please Try Again!")
            continue
if __name__ == "__main__":
    main()