class Warrior:
    def __init__(self, health=50, attack=5, defense=0):
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


class Defender(Warrior):
    def __init__(self, health=60, attack=3, defense=2):
        super().__init__()
        self.health = health
        self.attack = attack
        self.defense = defense

    def get_damage(self, damage):
        if damage > self.defense:
            self.health = self.health - (damage - self.defense)
            if self.health <= 0:
                self.is_alive = False


class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1


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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    unit_1 = Defender()
    unit_2 = Rookie()
    print(vars(unit_1))
    print(vars(unit_2))
    fight(unit_1, unit_2)
    assert unit_1.health == 60, unit_1.health

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

