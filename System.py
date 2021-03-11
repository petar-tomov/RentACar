from Car import Car
import json
from decimal import Decimal, ROUND_UP

class System:
    cost = 0
    toPop = False
    removeCar = 0
    brand = "Moskvich"  # brand and model will be used for printing information
    model = "412"
    cars = open('data.json')
    data = json.load(cars)
    cars.close()

    dataDict = {}
    for (k, v) in data.items():
        dataDict.update({k: v})

    carData = {}
    for c in dataDict:
        c = Car(dataDict[c]['brand'], dataDict[c]['model'],
                dataDict[c]['expense'], dataDict[c]['registry_num'],
                dataDict[c]['cost_per_hour'], dataDict[c]['cost_per_day'],
                dataDict[c]['cost_per_week'])
        carData.update({c.registry_num: c})

    def print_cars(self):
        print("Cars available for rent:")
        for c in System.carData.values():
            print(f"{c.brand} {c.model} with registry number {c.registry_num}")
            print(f"You can rent this car for ${c.cost_per_hour} per hour,"
                  f" ${c.cost_per_day} per day or ${c.cost_per_week} per week.\n")

    def rentacar_hours(self, customer, registry_num, hours):
        self.toPop = False
        for c in self.carData.keys():
            if registry_num == c:
                self.toPop = True
                self.cost = self.carData.get(c).cost_per_hour * hours
                self.removeCar = c
                customer.numRentedCars += 1
                customer.cost += self.cost
                self.brand = self.carData.get(c).brand
                self.model = self.carData.get(c).model
                print(f"{customer.name} has rented {self.brand} {self.model} "
                      f"for {hours} hours which will cost him ${self.cost}.\n")

        if self.toPop:
            self.carData.pop(self.removeCar)
        else:
            print(f"This car is not available for rent at the moment, {customer.name}!\n")

    def rentacar_day(self, customer, registry_num):
        self.toPop = False
        for c in self.carData.keys():
            if registry_num == c:
                self.toPop = True
                self.cost = self.carData.get(c).cost_per_day
                self.removeCar = c
                customer.numRentedCars += 1
                customer.cost += self.cost
                self.brand = self.carData.get(c).brand
                self.model = self.carData.get(c).model
                print(f"{customer.name} has rented {self.brand} {self.model} "
                      f"for a day which will cost him ${self.cost}.\n")

        if self.toPop:
            self.carData.pop(self.removeCar)
        else:
            print(f"This car is not available for rent at the moment, {customer.name}!\n")

    def rentacar_week(self, customer, registry_num):
        self.toPop = False
        for c in self.carData.keys():
            if registry_num == c:
                self.toPop = True
                self.cost = self.carData.get(c).cost_per_week
                self.removeCar = c
                customer.numRentedCars += 1
                customer.cost += self.cost
                self.brand = self.carData.get(c).brand
                self.model = self.carData.get(c).model
                print(f"{customer.name} has rented {self.brand} {self.model} "
                      f"for a week which will cost him ${self.cost}.\n")

        if self.toPop:
            self.carData.pop(self.removeCar)
        else:
            print(f"This car is not available for rent at the moment, {customer.name}!\n")

    def checkout(self, customer):
        print(f"{customer.name} has rented {customer.numRentedCars} cars in total.")
        if customer.numRentedCars >= 4:
            customer.cost *= 0.7
            customer.cost = Decimal(customer.cost).quantize(Decimal('.01'), rounding=ROUND_UP)
            print("A 30% discount will be applied for renting this amount of cars!")
        print(f"Money spent by {customer.name}: ${customer.cost}.")
        customer.numRentedCars = 0
        customer.cost = 0
        print("-------------------------------")
