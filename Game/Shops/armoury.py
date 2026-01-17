from Game.Fights.armoury import armoury_fight_sequence
import time as t

def armoury_shop_sequence(p, inv, weapons, armour, deada):
    dead = deada
    sword = None
    shield = None

    if not dead:
        print("a stern blacksmith glares at you, menacingly.")
        t.sleep(1)
        print("you look on the walls, seeing an assortment of swords and armour")
        t.sleep(1)
        print("'I will make it, if you can pay for it'")
    else:
        print("the workshop seems eerily quiet without his presence")
    t.sleep(1)
    print(f"you have {inv['gold']} gold")
    t.sleep(1)
    while True:
        try:
            choice = int(input("what do you do?\n"
                            "1) look at your options\n"
                            "2) buy a sword\n"
                            "3) buy armour\n"
                            "4) attack\n"
                            "5) exit\n"
                            ))
        except ValueError:
            print("that's not an option")
            continue
        else:
            if choice not in [1, 2, 3, 4, 5]:
                print("that is not an option")
                continue

        match choice:
            case 1:
                print("swords")
                t.sleep(0.3)
                for items in weapons:
                    print(items.name)
                    t.sleep(0.3)
                print("\narmour")
                t.sleep(0.3)
                for items in armour:
                    print(items.name)
                    t.sleep(0.3)
            case 2:
                for swords in weapons:
                    print(swords.name)
                    t.sleep(0.3)
                sword_choice = int(input("which sword do you want to buy?(1/2 etc): \n"))
                if sword_choice > len(weapons):
                    print("that is not an option")
                else:
                    sword = weapons[sword_choice - 1]
                    if sword.name == "Copper Sword":
                        if dead:
                            if input("steal the sword(y/n): ").lower() == "y":
                                print("you stole the sword")
                                return inv, dead, sword, shield
                        else:
                            print("'that will cost you 150 gold.")
                            if input("do you want to buy this sword?(y/n): ").lower == "y":
                                inv["gold"] -= 250
                                print("'alright, give me a minute'")
                                t.sleep(3)
                                print("'its done, use it well'")
                                t.sleep(1)
                                return inv, dead, sword, shield
                            else:
                                print("'alrighty.'")
                    elif sword.name == "Iron Sword":
                        if dead:
                            if input("steal the sword(y/n): ").lower() == "y":
                                print("you steal the sword")
                                return inv, dead, sword, shield
                        else:
                            print("'that will cost you 300 gold.")
                            if input("do you want to buy this sword?(y/n): ").lower == "y":
                                inv["gold"] -= 250
                                print("'alright, give me a minute'")
                                t.sleep(3)
                                print("'its done, use it well'")
                                t.sleep(1)
                                return inv, dead, sword, shield
                            else:
                                print("'alrighty.'")

            case 3:
                for armours in armour:
                    print(armours.name)
                    t.sleep(0.3)
                armour_choice = int(input("which armour do you want to buy?(1/2 etc): \n"))
                if armour_choice > len(weapons):
                    print("that is not an option")
                else:
                    shield = weapons[armour_choice - 1]
                    if shield.name == "leather":
                        if dead:
                            if input("steal the leather(y/n): ").lower() == "y":
                                print("you steal the leather")
                                return inv, dead, sword, shield
                        else:
                            print("'that will cost you 50 gold.")
                            if input("do you want to buy this armour?(y/n): ").lower == "y":
                                inv["gold"] -= 50
                                print("'alright, give me a minute'")
                                t.sleep(3)
                                print("'its done, use it well'")
                                t.sleep(1)
                                return inv, dead, sword, shield
                            else:
                                print("'alrighty.'")
                    elif shield.name == "chainmail":
                        if dead:
                            if input("steal the chainmail(y/n): ").lower() == "y":
                                print("you steal the chainmail")
                                return inv, dead, sword, shield
                        else:
                            print("'that will cost you 125 gold.")
                            if input("do you want to buy this armour?(y/n): ").lower == "y":
                                inv["gold"] -= 125
                                print("'alright, give me a minute'")
                                t.sleep(3)
                                print("'its done, use it well'")
                                t.sleep(1)
                                return inv, dead, sword, shield
                            else:
                                print("'alrighty.'")

                    elif shield.name == "iron":
                        if dead:
                            if input("steal the iron(y/n): ").lower() == "y":
                                print("you steal the iron")
                                return inv, dead, sword, shield
                        else:
                            print("'that will cost you 275 gold.")
                            if input("do you want to buy this armour?(y/n): ").lower == "y":
                                inv["gold"] -= 275
                                print("'alright, give me a minute'")
                                t.sleep(3)
                                print("'its done, use it well'")
                                t.sleep(1)
                                return inv, dead, sword, shield
                            else:
                                print("'alrighty.'")

            case 4:
                print("the man quickly deflects your strike with a hammer")
                t.sleep(2)
                print("'so you want to challenge me?'")
                t.sleep(2)
                print("'then lets fight'")
                t.sleep(1)
                print("he pulls out a chisel")
                t.sleep(1)
                fight_won, inv = armoury_fight_sequence(p, inv)
                if fight_won:
                    print("he groans in pain before collapsing to the floor, dead")
                    dead = True
                    t.sleep(1)
                    inv["gold"] += 1000
                    return inv, dead, sword, shield
                else:
                    print("the man laughs sternly")
                    t.sleep(1)
                    print("'nice try, come back later so we can spar again.'")
                    t.sleep(1)
                    return inv, dead, sword, shield

            case 5:
                print("the man hums deeply as you walk out")
                t.sleep(1)
                return inv, dead, sword, shield

            case _:
                print("not an option")