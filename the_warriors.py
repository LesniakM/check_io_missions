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


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.get_damage(unit_1.attack)
        if unit_2.is_alive:
            unit_1.get_damage(unit_2.attack)
    return unit_1.is_alive


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")
