class CapitalLocations:
    capitallocations_list =[]
    def __init__(self, name, amount, interest):
        self.name = name
        self.amount = amount
        self.interest = interest
        self.capitallocations_list.append(self)

#CapitalLocations defined by hand. Should be imported from JSON later.
Livret_A = CapitalLocations("Livret_A", 12000, 0.02)
Current = CapitalLocations("Current", 2700, 0)
OUT = CapitalLocations("Out", 0, 0)

class Movements:
    movements_list = []
    def __init__(self, name, from_location, to_location, amount, periodicity):
        self.name = name
        self.from_location = from_location
        self.to_location = to_location
        self.amount = amount #if negative, make negative
        self.periodicity = periodicity #defined in months
        self.movements_list.append(self)


def FindAmount(capital, interest):
    return capital*interest


#Movements define by hand. Should be imported from JSON later
rent = Movements("Rent", "Current", "OUT", 900, 1)
salary = Movements("Salary", "OUT", "Current", 2315.38, 1)
food = Movements("Food", "Current", "OUT", 500, 1)
Int_livret_a = Movements("LivA_interest", "OUT", "Livret_A", FindAmount(Livret_A.amount, Livret_A.interest), 12)
taxes = Movements("Taxes", "Current", "OUT", 3000, 12)

def Project(number_periods):
    for period in range(1,number_periods):
        for movement in Movements.movements_list:
            if period%movement.periodicity == 0:
                eval(movement.from_location).amount += -1 * movement.amount
                eval(movement.to_location).amount += movement.amount

Project(4)
print Livret_A.amount
print Current.amount
print OUT.amount
