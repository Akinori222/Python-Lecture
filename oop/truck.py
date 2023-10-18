from car import Car


class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_loading):
        super().__init__(model_name, mileage, manufacturer)
        self._max_loading = max_loading
        self._loadings = 0

    def load(self, weight):
        if weight > 0:
            self._loadings += weight
            print(f"carried {weight} tons of luggage.")
        else:
            if self._loadings <= -weight:
                self._loadings = 0
                print("I unloaded all my luggage.")
            else:
                self._loadings += weight
                print(f"unloaded {-weight} tons of luggage.")
        print(f"Current loading capacity is {self._loadings} tons")

        if self._loadings > self._max_loading:
            print(f"Maximum loading capacity is {self._max_loading} tons.")

truck = Truck("4tTruck", 6, "isuzu", 4)
# truck.gus()
truck.load(2)
truck.load(-1)
truck.load(4)
truck.load(-9)
