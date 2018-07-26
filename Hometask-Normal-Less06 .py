# coding: UTF-8

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:

    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health
        self.armor = armor
        self.damage = damage

    def calculate_damage(self, damage, armor):
        damage //= armor
        return damage

    def attack(self, opponent1, opponent2):
        damage = self.calculate_damage(opponent1.damage, opponent2.armor)
        opponent2.health -= damage
        print("{} нанес {} урона {}, у того осталось жизни {}.".format(opponent1.name, opponent2.name, damage, opponent2.health))

class Player(Person):
    def __init__(self, name, health, armor, damage):
        super().__init__(name, health, armor, damage)


class Enemy(Person):
    def __init__(self, name, health, armor, damage):
        super().__init__(name, health, armor, damage)


class Battle:
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def fight(self):
        last_attacker = self.attacker
        while self.attacker.health > 0 and self.defender.health > 0:
            if last_attacker == self.attacker:
                self.attacker.attack(self.attacker, self.defender)
                last_attacker = self.defender
            else:
                self.attacker.attack(self.defender, self.attacker)
                last_attacker = self.attacker

        if self.attacker.health <= 0:
            print(self.defender.name, " победил!")
        else:
            print(self.attacker.name, " победил!")


player_name = input("Введите имя первого игрока: ")
enemy_name = input("Введите имя второго игрока: ")

player = Player(player_name, 100, 1.2, 30)
enemy = Enemy(enemy_name, 80, 1.5, 40)
battle = Battle(player, enemy)

print("Сражаются ", player.name, " и ", enemy.name)
battle.fight()


