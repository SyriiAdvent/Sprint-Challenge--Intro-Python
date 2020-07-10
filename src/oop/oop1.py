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

####### VEHICLE #######

class Vehicle:
# Main class
  pass

####### FLIGHT VEHICLES #######

class FlightVehicle(Vehicle):
# base Class
  pass

class Starship(FlightVehicle):
  # sub Class
  pass

class Airplane(FlightVehicle):
  # sub Class
  pass

####### GROUND VEHICLES #######

class GroundVehicle(Vehicle):
# base Class
  pass

class Car(GroundVehicle):
# sub Class
  pass

class Motorcycle(GroundVehicle):
# sub Class
  pass
