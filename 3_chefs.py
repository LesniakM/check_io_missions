from abc import ABC, abstractmethod


class CookFactory(ABC):
    def __init__(self):
        self.food_cost = 0
        self.drink_cost = 0

    def add_food(self, amount: int, price: float) -> None:
        self.food_cost = self.food_cost + amount * price

    def add_drink(self, amount: int, price: float) -> None:
        self.drink_cost = self.drink_cost + amount * price

    @abstractmethod
    def total(self):
        pass


class JapaneseCook(CookFactory):
    def total(self) -> str:
        return f"Sushi: {self.food_cost}, Tea: {self.drink_cost}, Total: {self.drink_cost+self.food_cost}"


class RussianCook(CookFactory):
    def total(self) -> str:
        return f"Dumplings: {self.food_cost}, Compote: {self.drink_cost}, Total: {self.drink_cost + self.food_cost}"


class ItalianCook(CookFactory):
    def total(self) -> str:
        return f"Pizza: {self.food_cost}, Juice: {self.drink_cost}, Total: {self.drink_cost + self.food_cost}"


if __name__ == '__main__':
    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
