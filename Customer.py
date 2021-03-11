from System import System


class Customer:
    def __init__(self, name):
        self.name = name
        self.numRentedCars = 0
        self.cost = 0

    def check_catalogue(self):
        System.print_cars(System)
        print("")

    def rentacar_hours(self, car_registry, hours):
        System.rentacar_hours(System, self, car_registry, hours)

    def rentacar_day(self, car_registry):
        System.rentacar_day(System, self, car_registry)

    def rentacar_week(self, car_registry):
        System.rentacar_week(System, self, car_registry)

    def checkout(self):
        System.checkout(System, self)
