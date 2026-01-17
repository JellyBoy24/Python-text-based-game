import time as t
import random as rnd
from Game.entities import gladiator_A, gladiator_B, gladiator_C, gladiator_D

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
            print(f"{i}) {en.name} (HP: {round(en.hp, 2)}/{en.maxhealth}){marker}")
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





def arena_fight_sequence(p, inv):
    enemy_pool = [gladiator_A, gladiator_B, gladiator_C, gladiator_D]
    n_o_e = rnd.randint(1, 3)
    enemies = rnd.sample(enemy_pool, k=n_o_e)

    print("enemies emerge from the shadows of the training arena\n")
    t.sleep(1)
    for i, en in enumerate(enemies, 1):
        en.hp = en.maxhealth
        print(f"{i}) {en.name} (HP: {en.hp}/{en.maxhealth})")
        t.sleep(1)

    print("\n")

    while True:
        if all(en.hp <= 0 for en in enemies):
            print("all enemies are down")
            t.sleep(1)
            print("you win!")
            return True, inv
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
                print(f"{p.name} has dealt {round(damage_dealt, 2)} damage to the {target.name}")
                player_turn = False
                t.sleep(1)

            elif a == 2:
                p.defend()
                print(f"the first hit of damage received will be halved")
                player_turn = False


            elif a == 3:

                target = choose_target(enemies)

                if target is None:
                    continue

                damage_dealt = p.skill(target)

                if damage_dealt != 0.0:
                    print(f"{p.name} has used {p.weapon.skill_name}!")

                    t.sleep(1)

                    print(f"{p.name} has dealt {round(damage_dealt, 2)} damage to the {target.name}")

                    player_turn = False





            elif a == 4:

                try:
                    heal_opt = int(input(
                        f"1) low heal: {inv['apples']}\n2) med heal: {inv['heal_potions']}\n3) high heal: {inv['large_heal_potions']}\n4) full heal: {inv['full_heal']}\nwhich one do you want to use: "))
                except ValueError:
                    print(f"that's not an option!")
                    continue
                else:
                    if heal_opt not in [1, 2, 3, 4]:
                        print(f"that's not an option!")
                        continue

                match heal_opt:



                    case 1:

                        if p.hp == 100:

                            print(f"you can't do that")

                            continue



                        elif (inv.get("apples") or 0) > 0:

                            heal_amt = p.heal(5)

                            inv["apples"] -= 1

                            print(f"you ate an apple, and healed {heal_amt}")

                            player_turn = False


                        else:

                            print(f"you can't do that")

                            continue

                    case 2:

                        if p.hp == 100:

                            print(f"you can't do that")

                            continue


                        elif (inv.get("heal_potions") or 0) > 0:

                            heal_amt = p.heal(25)

                            inv["heal_potions"] -= 1

                            print(f"you drank a potion, and healed {heal_amt}")

                            player_turn = False


                        else:

                            print(f"you can't do that")

                            continue

                    case 3:

                        if p.hp == 100:

                            print(f"you can't do that")

                            continue


                        elif (inv.get("large_heal_potions") or 0) > 0:

                            heal_amt = p.heal(50)

                            inv["large_heal_potions"] -= 1

                            print(f"you drank a potion, and healed {heal_amt}")

                            player_turn = False


                        else:

                            print(f"you can't do that")

                            continue

                    case 4:

                        if p.hp == 100:

                            print(f"you can't do that")

                            continue


                        elif (inv.get("full_heal") or 0) > 0:

                            heal_amt = p.heal(100)

                            inv["full_heal"] -= 1

                            print(f"you drank a potion, and healed {heal_amt}")

                            player_turn = False


                        else:

                            print(f"you can't do that")

                            continue


            elif a == 5:
                target = choose_target(enemies)
                p.inspect(target)


        while not player_turn:
            for en in enemies:
                if en.hp <= 0:
                    continue
                else:
                    skill_use_chance = rnd.randint(1, 2)
                    if skill_use_chance == 1:
                        damage_dealt = en.attack(p)
                        print(f"{en.name} has dealt {round(damage_dealt, 2)} damage to the {p.name}")
                        t.sleep(1)
                        if p.hp <= 0:
                            print(f"you have lost")
                            return False, inv
                    else:
                        damage_dealt = en.skill(p)
                        if damage_dealt != 0.0:
                            print(f"{en.name} has used {en.weapon.skill_name}!")
                            t.sleep(1)
                            print(f"{en.name} has dealt {round(damage_dealt, 2)} damage to the {p.name}")
                            t.sleep(1)
                            if p.hp <= 0:
                                print(f"you have lost")
                                return False, inv

            player_turn = True
            t.sleep(1)


        #prints health bars
        print(f"{p.name}: {round(p.hp, 2)}/{p.maxhealth}")
        for i, en in enumerate(enemies, 1):
            print(f"{i}) {en.name}: {round(en.hp, 2)}/{en.maxhealth}")
        print("\n")



