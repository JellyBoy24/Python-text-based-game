from Game.Fights.secret import secret_fight_sequence
import time as t
from Game.objects import *
def secret_shop_sequence(p, inv, deads):
    dead = deads
    sword = None
    shields = None

    if not dead:
        print("a gloomy cloud of shadows emerge")
        t.sleep(1)
        print("'i see you have found me, very well done.'")
        t.sleep(1)
        print("'i will give you the best of the best, for a cost of course'")
        t.sleep(1)
    else:
        print("the sound of silence fills the air as the menacing cloud is nowhere to be found")
        t.sleep(1)
    print("you look on the wall, seeing one sword, and one set of armour")
    t.sleep(1)
    print(f"you have {inv['gold']} gold")
    t.sleep(1)
    while True:
        choice = int(input("what do you do?\n"
                           "1) buy the sword\n"
                           "2) buy the armour\n"
                           "3) attack\n"
                           "4) leave\n"
                           ))

        match choice:
            case 1:
                if dead:
                    if input("steal the sword?(y/n): ").lower() == "y":
                        sword = shadow_sword
                        return inv, dead, sword, shields
                    else:
                        print("you put the sword down")
                        return inv, dead, sword, shields
                else:
                    print("that shadow sword packs a hefty punch, but it costs 1,000")
                    if input("buy the sword?(y/n): ").lower() == "y":
                        if inv["gold"] < 1000:
                            print("you cant afford that")
                            return inv, dead, sword, shields
                        else:
                            sword = shadow_sword
                            inv["gold"] -= 1000
                            return inv, dead, sword, shields
                    else:
                        print("you put the sword down")
                        return inv, dead, sword, shields

            case 2:
                if dead:
                    if input("steal the armour?(y/n): ").lower() == "y":
                        shields = shadow_wall
                        return inv, dead, shields, shields
                    else:
                        print("you put the armour back")
                        return inv, dead, sword, shields
                else:
                    print("that shadow armour will make you almost invincible, for a small cost of 2,000 gold")
                    if input("buy the armour?(y/n): ").lower() == "y":
                        if inv["gold"] < 2000:
                            print("you cant afford that")
                            return inv, dead, sword, shields
                        else:
                            shields = shadow_wall
                            inv["gold"] -= 2000
                            return inv, dead, shields, shields
                    else:
                        print("you put the armour back")
                        return inv, dead, sword, shields




            case 3:
                print("you swing at the cloud, only for it to phase through him")
                t.sleep(2)
                print("'hmmm, you wish to fight?'")
                t.sleep(2)
                print("he floats infront of you")
                t.sleep(1)
                print("'lets see how you fare'")
                t.sleep(2)
                fight_won, inv = secret_fight_sequence(p, inv)

                if fight_won:
                    print("the cloud dissipates with a faint sigh, now dead")
                    dead = True
                    t.sleep(1)
                    inv["gold"] += 5000
                    return inv, dead, sword, shields
                else:
                    print("the shadowy cloud lets out a low chuckle")
                    t.sleep(1)
                    print("'you thought you could defeat me?'")
                    t.sleep(1)
                    print("'go away'")
                    return inv, dead, sword, shields
            case 4:
                print("the cloud fades, you walk out")
                t.sleep(1)
                return inv, dead, sword, shields

            case _:
                print("not an option")
                return inv, dead, sword, shields