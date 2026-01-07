import time as t
import random as rnd
from Game.entities import Entity, fighter_A,fighter_B,fighter_C

def choose_target(enemies):
    living = [en for en in enemies if en.hp > 0] # creates a new list for all living enemies
    if not living:
        return None
    elif len(living) == 1:
        return living[0] # when there is only one enemy left


    while True:
        print("choose a target")
        for i, en in enumerate(enemies, 1):
            marker = " (down)" if en.hp <= 0 else "" # displays (down) if an enemies health is 0
            print(f"{i}) {en.name} (HP: {en.hp}/{en.maxhealth}){marker}")
        try: # catches any errors
            target_choice = int(input("").strip()) # .strip() removes any whitespace
            if 1 <= target_choice <= len(enemies):
                target = enemies[target_choice - 1]
                if target.hp <= 0: # checks if target enemy is already down
                    print("that enemy is already down")
                    continue
                return target
            else:
                print("invalid choice")
        except ValueError:
            print("please enter a number")





def training_fight_sequence(p):
    enemy_pool = [fighter_A, fighter_B, fighter_C]
    n_o_e = rnd.randint(1, 3)
    enemies = rnd.sample(enemy_pool, k=n_o_e)

    print("enemies emerge from the shadows of the training arena\n")
    t.sleep(1)
    for i, en in enumerate(enemies, 1):
        print(f"{i}) {en.name} (HP: {en.hp}/{en.maxhealth})")
        t.sleep(1)

    print("\n")

    while True:
        if all(en.hp <= 0 for en in enemies):
            print("all enemies are down")
            t.sleep(1)
            print("you win!")
            return True
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
                target = choose_target(enemies)
                if target is None:
                    continue
                damage_dealt = p.attack(target)
                print(f"{p.name} has dealt {damage_dealt} damage to the {target.name}")
                player_turn = False
                t.sleep(1)

            elif a == 2:
                p.defend()
                print(f"all damage received will be halved")
                player_turn = False

            elif a == 3:
                target = choose_target(enemies)
                if target is None:
                    continue
                damage_dealt = p.skill(target)
                if damage_dealt == 0.0:
                    print(f"{p.name} tried to use {p.weapon.skill_name}")
                    t.sleep(1)
                    print(f"But it failed!")
                    t.sleep(1)
                    player_turn = False
                else:
                    print(f"{p.name} has used {p.weapon.skill_name}!")
                    t.sleep(1)
                    print(f"{p.name} has dealt {damage_dealt} damage to the {target.name}")
                    player_turn = False

            elif a == 4:
                heal_amt = p.heal(5)
                print(f"you ate an apple, and healed {heal_amt}")
                player_turn = False

            elif a == 5:
                target = choose_target(enemies)
                p.inspect(target)
                player_turn = False


        while not player_turn:
            for en in enemies:
                if en.hp <= 0:
                    continue
                else:
                    damage_dealt = en.skill(p)
                    if damage_dealt == 0.0:
                        damage_dealt = en.attack(p)
                        print(f"{en.name} has dealt {damage_dealt} damage to the {p.name}")
                        t.sleep(1)
                        if p.hp <= 0:
                            print(f"you have lost")
                            return False
                    else:
                        print(f"{en.name} has used {en.weapon.skill_name}!")
                        t.sleep(1)
                        print(f"{en.name} has dealt {damage_dealt} damage to the {p.name}")
                        t.sleep(1)
                        if p.hp <= 0:
                            print(f"you have lost")
                            return False

            player_turn = True


        #prints health bars
        print(f"{p.name}: {p.hp}/{p.maxhealth}")
        for i, en in enumerate(enemies, 1):
            print(f"{i}) {en.name}: {en.hp}/{en.maxhealth}")
        print("\n")



