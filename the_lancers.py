class Warrior:
    def __init__(self, health=50, attack=5, defense=0):
        self.is_alive = True
        self.health = health
        self.attack = attack
        self.defense = defense

    def get_damage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.is_alive = False

    def perform_attack(self, enemy, *args):
        enemy.get_damage(self.attack)


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


class Vampire(Warrior):
    def __init__(self, health=40, attack=4, vampirism=50):
        super().__init__()
        self.health = health
        self.attack = attack
        self.vampirism = vampirism

    def perform_attack(self, enemy, *args):
        enemy.get_damage(self.attack)
        self.health = self.health + (self.attack-enemy.defense) * self.vampirism // 100


class Lancer(Warrior):
    def __init__(self, health=50, attack=6):
        super().__init__()
        self.health = health
        self.attack = attack

    def perform_attack(self, enemy, enemy2=None):
        enemy.get_damage(self.attack)
        if enemy2:
            enemy2.get_damage(self.attack/2)


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
            army1_behind, army2_behind = None, None
            if len(army1.units) > 1:
                army1_behind = army1.units[1]
            if len(army2.units) > 1:
                army2_behind = army2.units[1]
            fight(army1.units[0], army2.units[0], army1_behind, army2_behind)
            if not army1.units[0].is_alive:
                army1.units.pop(0)
            if not army2.units[0].is_alive:
                army2.units.pop(0)
        return len(army1.units) > 0


def fight(unit_1, unit_2, unit_0=None, unit_3=None):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.perform_attack(unit_2, unit_3)
        if unit_2.is_alive:
            unit_2.perform_attack(unit_1, unit_0)
    return unit_1.is_alive


if __name__ == "__main__":
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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")