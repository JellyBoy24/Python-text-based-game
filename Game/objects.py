# this file creates the weapons, armour and (maybe) healing items
class Weapon:
    def __init__(self, name, damage, skill_name, skill_chance, skill_dmg) -> None:
        self.name = name
        self.damage = damage
        self.skill_name = skill_name
        self.skill_chance = skill_chance
        self.skill_dmg = skill_dmg

class Armour:
    def __init__(self, name, defence) -> None:
        self.name = name
        self.defence = defence # dmg reduction fraction (from 0-1)



nothing = Armour(name="None", defence=0)
leather = Armour(name="Leather", defence=0.1)
chainmail = Armour(name="Chainmail", defence=0.15)

#player weapons
fists = Weapon(name="Fists", damage=2, skill_name="Heavy attack", skill_chance=0.33, skill_dmg=10)
wood_sword = Weapon(name="Wooden Sword", damage=5, skill_name="slash flurry", skill_chance=0.25, skill_dmg=15)
iron_sword = Weapon(name="Iron Sword", damage=10, skill_name="steel piercer", skill_chance=0.2, skill_dmg=25)
obsidian_sword = Weapon(name="Obsidian Sword", damage=25, skill_name="diamond breaker", skill_chance=0.2, skill_dmg=75)
shadow_sword = Weapon(name="Shadow Sword", damage=50, skill_name="dark barrage", skill_chance=0.1, skill_dmg=100)
shadow_dagger = Weapon(name="Shadow Dagger", damage=15, skill_name="dark pierce", skill_chance=0.2, skill_dmg=35)

#tutorial weapons
    # line 8

#training weapons
    # line 9
shield = Weapon(name="Shield", damage=1, skill_name="shield bash", skill_chance=0.5, skill_dmg=5)
bow = Weapon(name="Bow", damage=4, skill_name="long shot", skill_chance=0.33, skill_dmg=12)



