class TaxiMeterCalculator:
    def __init__(self, distance,traffic):
        self.distance = distance
        self.traffic = traffic

    def priceCalculate(self):
            fee = 35 +(self.distance *10 )+(self.traffic *2 )
            return fee
         
    def showPrice(self):
        print("Your fee is  = ", self.priceCalculate() , " THB")

print("----Taxi Meter Calculator----")
val_distance = float(input("Enter distance : "))
val_traffic = float(input("Enter traffic mintues : "))

taxi = TaxiMeterCalculator(val_distance, val_traffic)
taxi.showPrice()
