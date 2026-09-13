# Parent class
class Vehicle:  # Parent class define     
    def __init__(self, brand, base_cost):  # Parent Constructor
        self.brand = brand
        self.__base_cost = base_cost # Private Attribute

    def __calculate_tax(self):
        return self.__base_cost * 0.10

    def get_total_price(self):
        tax = self.__calculate_tax()
        total_price = self.__base_cost + tax
        print(f"Brand : {self.brand}")
        print(f"Base Cost: {self.__base_cost}")
        print(self.__calculate_tax())
        print(f"Total Price : {total_price}")

# Child class
class ElectricCar(Vehicle):
    def __init__(self, brand, base_cost):
        super().__init__(brand, base_cost)
        
        
    def range(self):
        print(f"{self.brand}, Electric cars offer an average driving range of about 380 to 400 kilometers (235 to 250 miles) on a single charge.")
    
# Child class
class GasCar(Vehicle):
    def __init__(self, brand, base_count):
        super().__init__(brand, base_count)
        
    def gas(self):
        print(f"{self.brand}, The average fuel tank capacity for a standard passenger car ranges from 12 to 16 gallons (45 to 60 liters).") 

V1 = ElectricCar("Mustarg", 7800000)
V2 = GasCar("Maruti CGN", 45000)

print(" = "*30)
V1.get_total_price()
V1.range()
print(" = "*30)
V2.get_total_price()
V2.gas()