class Army:
    def __init__(self):
        self.nation = "unknown nation"

    def train_swordsman(self, name):
        return Swordsman(name, self.nation)

    def train_lancer(self, name):
        return Lancer(name, self.nation)

    def train_archer(self, name):
        return Archer(name, self.nation)


class Solider:
    def __init__(self, name, nation):
        self.name = name
        self.type = "Soldier"
        self.title = "Untitled"
        self.nation = nation

    def introduce(self):
        return f"{self.title} {self.name}, {self.nation} {self.type}"


class Swordsman(Solider):
    def __init__(self, name, nation):
        super().__init__(name, nation)
        self.type = "swordsman"
        if nation == "European":
            self.title = "Knight"
        elif nation == "Asian":
            self.title = "Samurai"
        else:
            print("Wrong nation!")


class Lancer(Solider):
    def __init__(self, name, nation):
        super().__init__(name, nation)
        self.type = "lancer"
        if nation == "European":
            self.title = "Raubritter"
        elif nation == "Asian":
            self.title = "Ronin"


class Archer(Solider):
    def __init__(self, name, nation):
        super().__init__(name, nation)
        self.type = "archer"
        if nation == "European":
            self.title = "Ranger"
        elif nation == "Asian":
            self.title = "Shinobi"


class AsianArmy(Army):
    def __init__(self):
        super().__init__()
        self.nation = "Asian"


class EuropeanArmy(Army):
    def __init__(self):
        super().__init__()
        self.nation = "European"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    print(soldier_1.introduce())

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
