from dataclasses import dataclass
import random


@dataclass
class RobotDTO:
    name: str
    price: int
    exists: bool
    count: int
    is_broken: bool


class Robot:
    def __init__(self, name: str, power: int, price: int):
        self.name = name
        self.power = power
        self.price = price
        self.exists = False
        self.count = 0
        self.is_broken = False

    def to_dto(self):
        return RobotDTO(
            name=self.name,
            price=self.price,
            count=self.count,
            exists=self.exists,
            is_broken=self.is_broken,
        )

    def check_for_breakdown(self):
        if self.count > 0 and not self.is_broken:
            if random.randint(1, 50) == 1:
                self.is_broken = True
                return True
            return False
