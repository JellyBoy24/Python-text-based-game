import time as t
from Game.entities import boss
import random as rnd



def boss_fight_sequence(p, inv):
    e = boss
    e.hp = e.maxhealth
    print(f"1) {e.name} (HP: {e.hp}/{e.maxhealth})\n")

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
                print(f"{p.name} has dealt {round(damage_dealt, 2)} damage to the {e.name}")
                if e.hp <= 0:
                    print(f"you have won!")
                    return True, inv
                player_turn = False
                t.sleep(1)

            elif a == 2:
                p.defend()
                print(f"the first hit of damage received will be halved")
                player_turn = False

            elif a == 3:
                damage_dealt = p.skill(e)
                if damage_dealt != 0.0:
                    print(f"{p.name} has used {p.weapon.skill_name}!")
                    t.sleep(1)
                    print(f"{p.name} has dealt {round(damage_dealt, 2)} damage to the {e.name}")
                    if e.hp <= 0:
                        print(f"you have won!")
                        return True, inv

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
                p.inspect(e)


        while not player_turn:
            skill_use_chance = rnd.randint(1,2)
            if skill_use_chance == 1:
                damage_dealt = e.attack(p)
                print(f"{e.name} has dealt {round(damage_dealt, 2)} damage to the {p.name}")
                if p.hp <= 0:
                    print(f"you have lost")
                    return False, inv
            else:
                damage_dealt = e.skill(p)
                if damage_dealt != 0.0:
                    print(f"{e.name} has used {e.weapon.skill_name}!")
                    t.sleep(1)
                    print(f"{e.name} has dealt {round(damage_dealt, 2)} damage to the {p.name}")
                    if p.hp <= 0:
                        print(f"you have lost")
                        return False, inv

            player_turn = True
            t.sleep(1)

        print(f"1) {e.name} (HP: {round(e.hp, 2)}/{e.maxhealth})\n")
        print(f"{p.name}: {round(p.hp, 2)}/{p.maxhealth}\n")