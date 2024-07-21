from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int, fuel: int, fuel_consumption: int):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption



    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Men4ik, your fuel is low, '
                                   'but your Mom is LOVE you)))')


    def move(self, distance: int | float):
        total_fuel = distance * self.fuel_consumption
        if total_fuel > self.fuel:
            raise NotEnoughFuel
        self.fuel -= total_fuel
