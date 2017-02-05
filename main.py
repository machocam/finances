#Global Variables
inflation = 0.02
increase_life_level = 0.05  #this should be in function of my net income increase - maybe 50% of that increase
increase_salary = 0.05

class CapitalLocations:
    capitallocations_list =[]
    def __init__(self, name, amount, interest):
        self.name = name
        self.amount = amount
        self.interest = interest
        self.capitallocations_list.append(self)

#CapitalLocations defined by hand. Should be imported from JSON later.
Livret_A = CapitalLocations("Livret_A", 12000, 0.02)
Current = CapitalLocations("Current", 2950, 0)
Bank = CapitalLocations("Bank", 0, 0)
Market = CapitalLocations("Market", 0, 0)
OUT = CapitalLocations("Out", 0, 0)

class Movements:
    movements_list = []
    def __init__(self, name, from_location, to_location, amount, periodicity):
        self.name = name
        self.from_location = from_location
        self.to_location = to_location
        self.amount = amount
        self.periodicity = periodicity #defined in months
        self.movements_list.append(self)
    
#Movements define by hand. Should be imported from JSON later
rent = Movements("Rent", "Current", "OUT", 900, 1)
salary = Movements("Salary", "OUT", "Current", 2315.38, 1)
food = Movements("Food", "Current", "OUT", 500, 1)
Int_livret_a = Movements("LivA_interest", "OUT", "Livret_A", 0, 12)
taxes = Movements("Taxes", "Current", "OUT", 3000, 12)
current_to_livret_a = Movements("current_to_livret", "Current", "Livret_A", 0, 1)

#Insert taxes calculation function here to have accurate taxes.

def calculate_movement_amounts(movement):
    if movement == rent or movement == food:
        movement.amount = movement.amount * (1+inflation)**(1/12) * (1+increase_life_level)**(1/12)
    elif movement == salary:
        movement.amount = movement.amount * (1+increase_salary)**(1/12)
    elif movement == current_to_livret_a:
        if Current.amount > 950: 
            movement.amount = Current.amount - 950
        else:
            movement.amount = 0
    elif movement == Int_livret_a:
        movement.amount = movement.amount * (1 + Livret_A.interest)
    #elif movement == taxes: 
        #here you will call the taxes function with all the current amounts

def Project(number_periods):
    for period in range(1,number_periods):
        for movement in Movements.movements_list:
            if period % movement.periodicity == 0:
                calculate_movement_amounts(movement)
                eval(movement.from_location).amount -= movement.amount
                eval(movement.to_location).amount += movement.amount
Project(24)
print Livret_A.amount
print Current.amount
print OUT.amount
