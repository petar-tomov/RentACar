from Car import Car
import json


class System:
    cost = 0

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
        carData.update({c.brand + c.model: c})

    def print_cars(self):
        print("You can currently rent:")
        for c in System.carData.values():
            print(f"{c.brand} {c.model} with registry number {c.registry_num}")
            print(f"You can rent this car for ${c.cost_per_hour} per hour,"
                  f" ${c.cost_per_day} per day or ${c.cost_per_week} per week.\n")
