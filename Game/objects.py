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


nothing = Armour(name="Nothing", defence=0)
leather = Armour(name="Leather", defence=0.1)
chainmail = Armour(name="Chainmail", defence=0.15)
iron = Armour(name="Iron", defence=0.33)
rock = Armour(name="Rock", defence=0.5)
obsidian = Armour(name="Obsidian", defence=0.7)
barrier = Armour(name="Barrier", defence=0.75)
shadow_wall = Armour(name="Shadows", defence=0.9)
scales = Armour(name="Scales", defence=0.65)

#player weapons
fists = Weapon(name="Fists", damage=2, skill_name="Heavy attack", skill_chance=0.33, skill_dmg=10)
wood_sword = Weapon(name="Wooden Sword", damage=5, skill_name="slash flurry", skill_chance=0.25, skill_dmg=15)
copper_sword = Weapon(name="Copper Sword", damage=7, skill_name="electrical current", skill_chance=0.25, skill_dmg=15)
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

#arena weapons
flail = Weapon(name="Flail", damage=7, skill_name="spike ball slam", skill_chance=0.2, skill_dmg=15)
duel_dagger = Weapon(name="Duel Dagger", damage=10, skill_name="slice and dice", skill_chance=0.15, skill_dmg=20)

#forest weapons
fairy_spell = Weapon(name="Fairy Spell", damage=25, skill_name="explosion", skill_chance=0.25, skill_dmg=45)
elemental_spell = Weapon(name="Elemental spell", damage=20, skill_name="boulder throw", skill_chance=0.20, skill_dmg=35)
wendigo_claws = Weapon(name="Claws", damage=15, skill_name="slash", skill_chance=0.33, skill_dmg=30)
claws = Weapon(name="Claws", damage=10, skill_name="slash and bite", skill_chance=0.25, skill_dmg=30)

#mini boss
club = Weapon(name="wooden club", damage=30, skill_name="Crater Slam", skill_chance=0.5, skill_dmg=45)

#boss weapons
fire = Weapon(name="Fire Breath", damage=35, skill_name="Incinerator", skill_chance=0.25, skill_dmg=60)
apple = Weapon(name="Apple", damage=45, skill_name="Seed Shot", skill_chance=0.25, skill_dmg=65)
chisel = Weapon(name="Chisel", damage=65, skill_name="Metal Chipper", skill_chance=0.2, skill_dmg=85)
potion = Weapon(name="Potion", damage=45, skill_name="Poison toss", skill_chance=0.33, skill_dmg=65)
shadows = Weapon(name="Shadows", damage=55, skill_name="Sombre Rebellion", skill_chance=0.2, skill_dmg=95)