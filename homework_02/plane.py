
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, max_cargo, cargo):
        super().__init__(max_cargo)
        self.cargo = cargo

    def load_cargo(self, numbers: int):
        if numbers + self.cargo > self.max_cargo:
            raise CargoOverload

        self.cargo += numbers

    def remove_all_cargo(self) -> int:
        zeroing = self.cargo * 0
        return zeroing
