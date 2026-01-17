# this file creates all the entities/npcs and enemies needed on the game

from Game.objects import *
import time as t
import random as rnd

#overarching entity template
class Entity:
    def __init__(self, level: int, name: str, hp: int, armour: Armour, weapon: Weapon):
        self.level = level
        self.name = name
        self.hp = hp
        self.maxhealth = hp

        self.weapon = weapon

        self.armour = armour
        self.defending = False

    def attack(self, target: "Entity") -> float:
        dmg = self.weapon.damage

        if not target.defending:
            damage = dmg
        else:
            damage = dmg/2

            target.defending = False

        final_damage = damage * (1-target.armour.defence)
        target.hp = max(target.hp -  final_damage, 0)
        return final_damage

    def defend(self):
        self.defending = True

    def skill(self, target: "Entity") -> float:

        if rnd.random() < self.weapon.skill_chance:

            dmg = self.weapon.skill_dmg
            if not target.defending:
                damage = dmg

            else:
                damage = dmg / 2

                target.defending = False
            final_damage = damage * (1 - target.armour.defence)
            target.hp = max(target.hp - final_damage, 0)
            return final_damage
        else:
            print(f"{self.name} tried to use {self.weapon.skill_name}")
            t.sleep(1)
            print(f"But it failed!")
            t.sleep(1)
            final_damage = 0.0
            return final_damage

    def heal(self, heal: int):
        self.hp += heal
        if self.hp > self.maxhealth:
            self.hp = self.maxhealth
        return heal

    def inspect(self, target: "Entity") -> bool:
        print(f"the enemy is called {target.name}")
        t.sleep(1)
        print(f"its max hp is {target.maxhealth}")
        t.sleep(1)
        print(f"its current hp is {target.hp}")
        t.sleep(1)
        print(f"its attack appears to be {target.weapon.damage}")
        t.sleep(1)
        print(f"it can use a skill called {target.weapon.skill_name}")
        t.sleep(1)
        print(f"the chance of {target.weapon.skill_name} is {target.weapon.skill_chance}")
        t.sleep(1)
        print(f"the skill deals {target.weapon.skill_dmg} damage")
        t.sleep(1)
        print(f"the {target.name} is wearing {target.armour.name} armour which reduces damage by {target.armour.defence * 100}%")
        t.sleep(1)
        return True

#tutorial
dummy = Entity(level=1, name ="Training Dummy", hp = 15, armour=nothing, weapon = fists)

#training
fighter_A = Entity(level=3, name="Shield fighter", hp=35, armour=chainmail, weapon=shield)
fighter_B = Entity(level=5, name="Sword fighter", hp=25, armour = leather, weapon = wood_sword)
fighter_C = Entity(level=2, name="Bow fighter", hp = 20, armour=nothing, weapon=bow)

#forest
fairy = Entity(level=7, name="Fairy", hp=10, armour=nothing, weapon=fairy_spell)
elemental = Entity(level=8, name="Elemental spirit", hp=35, armour=rock, weapon=elemental_spell)
wendigo = Entity(level=10, name="Wendigo", hp=65, armour=nothing, weapon=wendigo_claws)
wolf = Entity(level=8, name="Wolf", hp=35, armour=nothing, weapon=claws)

#arena
gladiator_A = Entity(level=8, name="Flail swinger", hp=25, armour=iron, weapon=flail)
gladiator_B = Entity(level=6, name="Dagger wielder", hp=30, armour=leather, weapon=duel_dagger)
gladiator_C = Entity(level=10, name="Champion Fighter", hp=75, armour=nothing, weapon=iron_sword)
gladiator_D = Entity(level=3, name="cowardly warrior", hp=35, armour=chainmail, weapon=bow)

#market boss
market_keeper = Entity(level=50, name="Granny Smith", hp=250, armour=nothing, weapon=apple)

#armoury boss
armoury_keeper = Entity(level=75, name="Muscular blacksmith", hp=200, armour=iron, weapon=chisel)

#potion boss
potion_keeper = Entity(level = 65, name="Divine Alchemist", hp=100, armour=barrier, weapon=potion)

#secret boss
secret_keeper = Entity(level=100, name="Mysterious Entity", hp=250, armour=shadow_wall, weapon=shadows)

#mini boss
mini_boss = Entity(level=25, name="Giant Orc", hp=100, armour=leather, weapon=club)

#Final Boss
boss = Entity(level=50, name="Dragon", hp=150, armour=scales, weapon=fire)


#alleyway fight
bandit_A = Entity(level=4, name="wanted murderer", hp=30, armour=nothing, weapon=iron_sword)
bandit_B = Entity(level=4, name="knife criminal", hp=25, armour=nothing, weapon=duel_dagger)