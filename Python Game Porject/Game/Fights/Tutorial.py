import time as t
import random as rnd


def tutorial_fight_sequence(p, e):
    apples = 0
    print(f"the {e.name} stands before you to fight")
    while True:
        player_turn = True
        while player_turn:
            try:
                a = int(input(f"1) attack\n2) defend\n3) skill\n4) item\n5) Inspect\nwhat will you do: "))
            except ValueError:
                print(f"that's not an option!")
                continue
            else:
                if a not in [1,2,3,4,5]:
                    print(f"that's not an option!")
                    continue

            if a == 1:
                damage_dealt = p.attack(e)
                print(f"{p.name} has dealt {damage_dealt} damage to the {e.name}")
                if e.hp <= 0:
                    print(f"you have won!")
                    return True
                player_turn = False
                t.sleep(1)

            elif a == 2:
                p.defend()
                print(f"all damage received will be halved")
                player_turn = False

            elif a == 3:
                skill_use_chance = rnd.randint(1,3)
                if skill_use_chance != 3:
                    print(f"{p.name} tried to use {p.skill_name}")
                    t.sleep(1)
                    print(f"and it Failed!")
                    t.sleep(1)
                    player_turn = False
                else:
                    damage_dealt = p.skill(e, "heart piercer", 15)
                    print(f"{p.name} has used {p.skill_name}!")
                    t.sleep(1)
                    print(f"{p.name} has dealt {damage_dealt} damage to the {e.name}")
                    player_turn = False

            elif a == 4:
                p.heal(5)
                print(f"you ate an apple, and healed {e.name}")
                apples += 1
                player_turn = False

            elif a == 5:
                p.inspect(e)
                player_turn = False


        while not player_turn:
            skill_use_chance = rnd.randint(1,5)
            if skill_use_chance != 5:
                damage_dealt = e.attack(p)
                print(f"{e.name} has dealt {damage_dealt} damage to the {p.name}")
                if p.hp <= 0:
                    print(f"you have lost")
                    return False

            else:
                damage_dealt = e.skill(p, "Heavy Attack", 5)
                print(f"{e.name} has used {e.skill_name}!")
                t.sleep(1)
                print(f"{e.name} has dealt {damage_dealt} damage to the {p.name}")
                if p.hp <= 0:
                    print(f"you have lost")
                    return False

            player_turn = True
            t.sleep(1)

        print(f"health of {p.name}: {p.hp}/{p.maxhealth}")
        print(f"health of {e.name}: {e.hp}/{e.maxhealth}")

