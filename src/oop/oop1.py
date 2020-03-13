# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class for all vehicles

class Vehicle:
    def __init__(self):
        pass

# Base class for flight vehicles

class FlightVehicle(Vehicle):
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        pass

# Base class for starship vehicles

class Starship(FlightVehicle):
    def __init__(self):
        pass

# Base class for ground vehicles

class GroundVehicle(Vehicle):
    def __init__(self):
        super().__init__()
    pass

class Car(GroundVehicle):
    def __init__(self):
        super().__init__()
    pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        super().__init__()
    pass