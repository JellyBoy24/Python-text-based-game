# this file creates all the entities/npcs and enemies needed on the game

from Game.objects import *
import time as t
#overarching entity template
class Entity:
    def __init__(self, level: int, name: str, hp: int, armour: Armour, weapon: Weapon):
        self.level = level
        self.name = name
        self.hp = hp
        self.maxhealth = hp

        self.weapon = weapon
        self.skill_name = ""
        self.skill_damage = 0

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

    def skill(self, target: "Entity", skill_name: str, skill_damage: int) -> float:
        self.skill_name = skill_name
        self.skill_damage = skill_damage

        dmg = self.skill_damage
        if not self.defending:
            damage = dmg

        else:
            damage = dmg/2

            target.defending = False
        final_damage = damage * (1-target.armour.defence)
        target.hp = max(target.hp - final_damage, 0)
        return final_damage

    def heal(self, heal: int):
        self.hp += heal
        if self.hp > self.maxhealth:
            self.hp = self.maxhealth
        return heal

    def inspect(self, target: "Entity") -> None:
        print(f"the enemy is called {target.name}")
        t.sleep(1)
        print(f"its max hp is {target.maxhealth}")
        t.sleep(1)
        print(f"its current hp is {target.hp}")
        t.sleep(1)
        print(f"its attack appears to be {target.weapon.damage}")
        t.sleep(1)





Dummy = Entity(level=1, name ="Training Dummy", hp = 25, armour=nothing, weapon = fists)

