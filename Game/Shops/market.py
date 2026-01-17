from Game.Fights.market import market_fight_sequence
import time as t

def market_shop_sequence(p, inv, deadm):
    dead = deadm
    if not dead:
        print("a sweet old lady welcomes you")
        t.sleep(1)
    else:
        print("the sound of silence fills the air as the granny is no longer there")
        t.sleep(1)
    print("you look infront of you, seeing a crate of apples")
    t.sleep(1)
    print(f"you have {inv['gold']} gold")
    t.sleep(1)
    while True:
        try:
            choice = int(input("what do you do?\n"
                           "1) buy an apple for 10 gold\n"
                           "2) buy 10 apples for 100 gold\n"
                           "3) attack\n"
                           "4) leave\n"
                           ))
        except ValueError:
            print("that is not an option")
            continue
        else:
            if choice not in [1, 2, 3, 4]:
                print("that is not an option")
                continue

        match choice:
            case 1:
                if dead:
                    print("you steal an apple")
                    inv["apples"] += 1
                else:
                    if inv["gold"] < 10:
                        print("you cant afford that")
                    else:
                        print("you buy an apple")
                        inv["gold"] -= 10
                        inv["apples"] += 1
                return inv, dead
            case 2:
                if dead:
                    print("you steal 10 apples")
                    inv["apples"] += 10
                else:
                    if inv["gold"] < 100:
                        print("you cant afford that")
                    else:
                        print("you buy 10 apples")
                        inv["gold"] -= 100
                        inv["apples"] += 10
                return inv, dead
            case 3:
                print("the old lady effortlessly dodges")
                t.sleep(2)
                print("'so its like that dear?'")
                t.sleep(2)
                print("'so be it'")
                t.sleep(1)
                print("'Lets fight'")
                t.sleep(1)
                fight_won, inv = market_fight_sequence(p, inv)
                if fight_won:
                    print("the old lady falls to the floor, dead")
                    dead = True
                    t.sleep(1)
                    inv["gold"] += 1000
                    return inv, dead
                else:
                    print("the old lady chuckles")
                    t.sleep(1)
                    print("'better luck next time'")
                    t.sleep(1)
                    return inv, dead
            case 4:
                print("the old lady sees you out")
                t.sleep(1)
                return inv, dead

            case _:
                print("not an option")