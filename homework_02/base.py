from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight: int = 0, started: int, fuel: int = 0, fuel_consumption: int = 0):
        self.weight = weight
        # self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        if not self.started:
            if self.started > 0:
                self.started = True
            else:
                raise LowFuelError


    def move(self, distance: int):
        total_fuel = distance * self.fuel_consumption
        if total_fuel > distance:
            raise NotEnoughFuel
        self.fuel -= total_fuel