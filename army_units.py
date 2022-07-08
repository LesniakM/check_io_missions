from abc import ABC, abstractmethod


# Would like to name this class ArmyFactory, but then it would not pass the tests on checkio.org.
class Army(ABC):
    @abstractmethod
    def __init__(self):
        self.nation = "nation"

    @property
    def army_type(self):
        return "army type"

    def train_swordsman(self, name):
        return Swordsman(name, self.nation)

    def train_lancer(self, name):
        return Lancer(name, self.nation)

    def train_archer(self, name):
        return Archer(name, self.nation)


class SoliderFactory(ABC):
    @abstractmethod
    def __init__(self, name, nation):
        self.name = name
        self.nation = nation
        self.type = "Soldier"
        self.title = "Untitled"

    def introduce(self):
        return f"{self.title} {self.name}, {self.nation} {self.type}"


class AsianArmy(Army):
    def __init__(self):
        self.nation = "Asian"


class EuropeanArmy(Army):
    def __init__(self):
        self.nation = "European"


class Swordsman(SoliderFactory):
    def __init__(self, name, nation):
        self.name = name
        self.nation = nation
        self.type = "swordsman"
        if nation == "European":
            self.title = "Knight"
        elif nation == "Asian":
            self.title = "Samurai"


class Lancer(SoliderFactory):
    def __init__(self, name, nation):
        self.name = name
        self.nation = nation
        self.type = "lancer"
        if nation == "European":
            self.title = "Raubritter"
        elif nation == "Asian":
            self.title = "Ronin"


class Archer(SoliderFactory):
    def __init__(self, name, nation):
        self.name = name
        self.nation = nation
        self.type = "archer"
        if nation == "European":
            self.title = "Ranger"
        elif nation == "Asian":
            self.title = "Shinobi"


if __name__ == '__main__':
    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"
