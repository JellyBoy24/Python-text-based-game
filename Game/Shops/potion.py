from Game.Fights.potion import potion_fight_sequence
import time as t

def potion_shop_sequence(p, inv, deadp):
    dead = deadp
    sword = None
    shield = None

    print("a hyperactive alchemist runs up to you.")
    t.sleep(1)
    print("'you look like you could use some healing potions'")
    t.sleep(1)
    print("'I will make it, if you can pay for it'")
    t.sleep(1)
    print(f"you have {inv['gold']} gold")
    t.sleep(1)
    while True:
        try:
            choice = int(input("what do you do?\n"
                           "1) buy a health potion\n"
                           "2) buy a large health potion\n"
                           "3) buy a full heal\n"
                           "4) attack\n"
                           "5) exit\n"
                           ))
        except ValueError:
            print("that is not an option")
            continue
        else:
            if choice not in [1, 2, 3, 4, 5]:
                print("that is not an option")
                continue

        match choice:
            case 1:
                if dead:
                    if input("steal a health potion?(y/n): ").lower() == "y":
                        inv["heal_potions"] += 1
                        return inv, dead
                else:
                    print("'that will cost you 50 gold.'")
                    buy = input("buy?(y/n): ")
                    if buy.lower() == "y":
                        inv["gold"] -= 50
                        inv["heal_potions"] += 1
                        return inv, dead
            case 2:
                if dead:
                    if input("steal a large health potion?(y/n): ").lower() == "y":
                        inv["large_heal_potions"] += 1
                        return inv, dead
                else:

                    print("that will cost you 200 gold.")
                    buy = input("buy?(y/n): ")
                    if buy.lower() == "y":
                        inv["gold"] -= 200
                        inv["large_heal_potions"] += 1
                        return inv, dead

            case 3:
                if dead:
                    if input("steal a full heal?(y/n): ").lower() == "y":
                        inv["full_heal"] += 1
                        return inv, dead
                else:

                    print("that will cost you 350 gold.")
                    buy = input("buy?(y/n): ")
                    if buy.lower() == "y":
                        inv["gold"] -= 350
                        inv["full_heal"] += 1
                        return inv, dead
            case 4:
                print("the man frantically dodges")
                t.sleep(2)
                print("'how dare you attack me in my own abode'")
                t.sleep(2)
                print("'lets fight then'")
                t.sleep(1)
                print("he pulls out vials of a green looking substance, poison?")
                t.sleep(1)
                fight_won, inv = potion_fight_sequence(p, inv)
                if fight_won:
                    print("he groans in pain before collapsing to the floor, dead")
                    dead = True
                    t.sleep(1)
                    inv["gold"] += 1000
                    return inv, dead
                else:
                    print("the man laughs crazily")
                    t.sleep(1)
                    print("'i win and you lose haha'")
                    t.sleep(1)
                    return inv, dead

            case 5:
                print("the man chuckles maniacally as you walk out")
                t.sleep(1)
                print("'come back again soon'")
                return inv, dead

            case _:
                print("not an option")