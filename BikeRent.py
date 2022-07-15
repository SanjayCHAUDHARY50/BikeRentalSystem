class BikeRentalCompany:
    def __init__(self, stocks):
        self.stocks = stocks
    
    def available(self):
        print("The available no. of bikes : ", self.stocks)
      
    def hour_options(self, k):
        if self.stocks >= k:
            temp = input("Enter the no. of hours you need bikes for rent : ")
            try:
                temp = int(temp)
            except ValueError:
                print("Enter the correct value")
                return None
            print("Total Amount you have to pay : ", 10*k*temp)
            self.stocks -= k
            return 10*k*temp
        elif k <= 0:
            print("Enter the correct value...")
            return None
        else:
            print(str(k) + " Bikes are not available...")
            return None
        
        
    def daily_options(self, k):
        if self.stocks >= k:
            temp = input("Enter the no. of days you need bikes for rent : ")
            try:
                temp = int(temp)
            except ValueError:
                print("Enter the correct value")
                return None
            print("Total Amount you have to pay : ", 100*k*temp)
            self.stocks -= k
            return 100*k*temp
        elif k <= 0:
            print("Enter the correct value...")
            return None
        else:
            print(str(k) + " Bikes are not available...")
            return None
        
        
    def week_options(self, k):
        if self.stocks >= k:
            temp = input("Enter the no. of weeks you need bikes for rent : ")
            try:
                temp = int(temp)
            except ValueError:
                print("Enter the correct value")
                return None
            print("Total Amount you have to pay : ", 500*k*temp)
            self.stocks -= k
            return 500*k*temp
        elif k <= 0:
            print("Enter the correct value...")
            return None
        else:
            print(str(k) + " Bikes are not available...")
            return None
            
            
          
    
        
                        

                
                
            
                        
        