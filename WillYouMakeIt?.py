average_car = 25 # miles per gallon
nearest_pump = 50 # miles to the nearest pump
gallons = 2 # gallons of fuel left


def make_it():
    max_distance = gallons * average_car
    if max_distance >= nearest_pump:
        return True
    else:
        return False

print(make_it())
    
