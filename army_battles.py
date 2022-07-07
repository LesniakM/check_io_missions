class Warrior:
    def __init__(self, health=50, attack=5):
        self.is_alive = True
        self.health = health
        self.attack = attack

    def get_damage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.is_alive = False


class Knight(Warrior):
    def __init__(self, attack=7):
        super().__init__()
        self.attack = attack


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type=Warrior, number=1):
        for n in range(number):
            self.units.append(unit_type())


class Battle:
    @staticmethod
    def fight(army1, army2):
        while len(army1.units) > 0 and len(army2.units) > 0:
            fight(army1.units[0], army2.units[0])
            if not army1.units[0].is_alive:
                army1.units.pop(0)
            if not army2.units[0].is_alive:
                army2.units.pop(0)
        return len(army1.units) > 0


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.get_damage(unit_1.attack)
        if unit_2.is_alive:
            unit_1.get_damage(unit_2.attack)
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False


    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")