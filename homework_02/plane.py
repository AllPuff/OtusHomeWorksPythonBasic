
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, fuel, weight, fuel_consumption, max_cargo):
        super().__init__(fuel, weight, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        if self.cargo + weight > self.max_cargo:
            raise CargoOverload

        self.cargo += weight

    def remove_all_cargo(self) -> int:
        weight = self.cargo
        self.cargo = 0
        return weight
