from dataclasses import dataclass


@dataclass
class RobotDTO:
    name: str
    price: int
    how_many: int
    exists: bool


class Robot:
    def __init__(self, name: str, power: int, price: int, exists: bool, how_many: int):
        self.name = name
        self.power = power
        self.price = price
        self.exists = exists
        self.how_many = how_many

    def to_dto(self):
        return RobotDTO(
            name=self.name, price=self.price, how_many=self.how_many, exists=self.exists
        )
