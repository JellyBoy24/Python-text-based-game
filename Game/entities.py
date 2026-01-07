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
        return True

#tutorial
dummy = Entity(level=1, name ="Training Dummy", hp = 25, armour=nothing, weapon = fists)

#training
fighter_A = Entity(level=3, name="Shield fighter", hp=65, armour=chainmail, weapon=shield)
fighter_B = Entity(level=5, name="Sword fighter", hp=50, armour = leather, weapon = wood_sword)
fighter_C = Entity(level=2, name="ranged Fighter", hp = 35, armour=nothing, weapon=bow)