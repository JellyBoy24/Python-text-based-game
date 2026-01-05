import time as t
import random as rnd



def training_fight_sequence(p, e):
    while True:
        p.attack(e)
        print(f"{p.name} has dealt {p.weapon.damage} damage to the {e.name}")
        t.sleep(1)
        skill_use = rnd.randint(1,10)
        if skill_use != 10:
            e.attack(p)
            print(f"{e.name} has dealt {e.weapon.damage} damage to the {p.name}")
            skill_use += 1
        else:
            e.skill(p, "Heavy Attack", 10)
            print(f"{e.name} has used {e.skill_name}!")
            t.sleep(1)
            print(f"{e.name} has dealt {e.skill_damage} to the {p.name}")
        t.sleep(1)

        print(f"health of {p.name}: {p.hp}/{p.maxhealth}")
        print(f"health of {e.name}: {e.hp}/{e.maxhealth}")

        if p.hp <= 0:
            print(f"you have died!")
            return False
        elif e.hp <= 0:
            print(f"you have won!")
            return True

        input()