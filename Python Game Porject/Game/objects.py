class Weapon:
    def __init__(self, name, damage) -> None:
        self.name = name
        self.damage = damage

class Armour:
    def __init__(self, name, defence) -> None:
        self.name = name
        self.defence = defence # dmg reduction fraction (from 0-1)



nothing = Armour(name="None", defence=0)
leather = Armour(name="Leather", defence=0.1)

#player weapons
fists = Weapon(name="Fists", damage=2)
wood_sword = Weapon(name="Wooden Sword", damage=5)
iron_sword = Weapon(name="Iron Sword", damage=10)
obsidian_sword = Weapon(name="Obsidian Sword", damage=25)
shadow_sword = Weapon(name="Shadow Sword", damage=50)
shadow_dagger = Weapon(name="Shadow Dagger", damage=15)

#tutorial weapons
    # line 8

#training weapons
    # line 9
shield = Weapon(name="Shield", damage=1)
bow = Weapon(name="Bow", damage=4)



