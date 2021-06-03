class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Orc(Enemy):
    def __init__(self):
        self.name = "Orc"
        self.hp = 20
        self.damage = 5


class Goblin(Enemy):
    def __init__(self):
        self.name = "Goblin"
        self.hp = 5
        self.damage = 1


class MischiefOfRats(Enemy):
    def __init__(self):
        self.name = "Mischief of rats"
        self.hp = 50
        self.damage = 4


class GiantSpider(Enemy):
    def __init__(self):
        self.name = "Giant Spider"
        self.hp = 10
        self.damage = 2
