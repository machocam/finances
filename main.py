class CapitalLocations:
    def __init__(self, name, amount, interest):
        self.name = name
        self.amount = amount
        self.interest = interest

#CapitalLocations defined by hand. Should be imported from JSON later.
location1 = CapitalLocations("Livret_A", 12000, 0.02)
location2 = CapitalLocations("Current", 2700, 0)

class Movement:
    def __init__(self, name, from_location, to_location, amount, periodicity):
        self.name = name
        self.from_location = from_location
        self.to_location = to_location
        self.amount = amount #if negative, make negative
        self.periodicity = periodicity #defined in months


def FindAmount(capital, interest):
    return capital*interest


#Movements define by hand. Should be imported from JSON later
movement1 = Movement("Rent", "Current", "OUT", -900, 1)
movement2 = Movement("Salary", "OUT", "Current", 2315.38, 1)
movement3 = Movement("Food", "Current", "OUT", -500, 1)
movement4 = Movement("LivA_interest", "OUT", "Livret_A", FindAmount(location1.amount, location1.interest), 12)
movement5 = Movement("Taxes", "Current", "OUT", -3000, 12) 
