class ATM: # define class
    branch_location1 = "SBI Bank, Laxamivadi Main Road, Rajkot" # class Attribute
    branch_location2 = "ICICI Bank, Palace Road, Rajkot"

    def __init__(self, name, acc_no, pin):    # Constructor
        self.name = name
        self.acc_no = acc_no
        self.__pin = pin # private attribute

    def __check_pin(self, entry_pin):  # private method
        return self.__pin == entry_pin

    def withdraw_cash(self, entry_pin):    #instance method
        if self.__check_pin(entry_pin):    # private method called
            print("✅ PIN is Correct")
            print(f"Name: {self.name} | A/c no: {self.acc_no} | Money withdrawn successfully.\nThank You 😀")
            
        else:
            print(f"❌ PIN is Wrong !!!")

    @staticmethod   #staticmethod
    def safety():
        print("👮 Always inspect the ATM for loose parts or skimming devices, and shield the keypad with your hand while entering your PIN.")

# object 
ATM1 = ATM("Dhirubhai", 1234567890, 2390) 
ATM2 = ATM("Rajubhai",  4904403124, 2390)

# execution
print("="*30)
print(ATM1.branch_location1)
ATM1.withdraw_cash(2390)
ATM1.safety()

print("\n"+"="*30)
print(ATM2.branch_location2)
ATM2.withdraw_cash(1390)
ATM2.safety()