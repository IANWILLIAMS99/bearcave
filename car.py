class Vehicle:

  def __init__(self, make, model, year, weight):
    self.make = make
    self.model = model
    self.year = year
    self.weight = weight

  def get_make(self):
    return self.make

  def get_model(self):
    return self.model

  def get_year(self):
    return self.year

  def get_weight(self):
    return self.weight


class Car(Vehicle):

  def __init__(self, make, model, year, weight, num_doors):
    Vehicle.__init__(self, make, model, year, weight)
    self.num_doors = num_doors

  def get_doors(self):
    return self.num_doors


class Pickup(Vehicle):

  def __init__(self, make, model, year, weight, drive_type):
    Vehicle.__init__(self, make, model, year, weight)
    self.drive_type = drive_type

  def get_drive_type(self):
    return self.drive_type


garage = []

while True:
  print("1. Add a car")
  print("2. Add a pickup truck")
  print("3. Quit")
  user_input = int(input("Enter your choice: "))

  if user_input == 1:
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year = input("Enter car year: ")
    weight = input("Enter car weight: ")
    num_doors = input("Enter number of doors: ")
    car = Car(make, model, year, weight, num_doors)
    garage.append(car)
  elif user_input == 2:
    make = input("Enter pickup truck make: ")
    model = input("Enter pickup truck model: ")
    year = input("Enter pickup truck year: ")
    weight = input("Enter pickup truck weight: ")
    drive_type = input("Enter drive type: ")
    pickup = Pickup(make, model, year, weight, drive_type)
    garage.append(pickup)
  else:
    break

for vehicle in garage:
  print("Make:", vehicle.get_make())
  print("Model:", vehicle.get_model())
  print("Year:", vehicle.get_year())
  print("Weight:", vehicle.get_weight())
  if isinstance(vehicle, Car):
    print("Number of doors:", vehicle.get_doors())
  elif isinstance(vehicle, Pickup):
    print("Drive type:", vehicle.get_drive_type())
  print("\n")
