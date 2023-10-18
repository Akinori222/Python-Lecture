class Car:
    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gus(self):
        print(f"{self.model_name}/(Fuel efficiency:{self.mileage}) STart!!")

    def brakes(self):
        print(f"{self.model_name}/(Fuel efficiency:{self.mileage}) Breaks!")
        print("{0.model_name}/(Fuel efficiency:{0.mileage}) Breaks!".format(self))


benz = Car("Benz", 15, "Mercedes-benz")

if __name__ == "__main__":
    print(benz.model_name)
    benz.gus()