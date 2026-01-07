from Game.entities import *
from Fights.training import training_fight_sequence
from Fights.tutorial import tutorial_fight_sequence
from Game.objects import *
import time as t


class Player(Entity):
    def __init__(self, level, name, hp: int, armour: Armour, weapon: Weapon, position):
        self.position = position
        super().__init__(level, name, hp, armour, weapon)


def in_bounds(x, y, lmap):
    return 0 <= y < len(lmap) and 0 <= x < len(lmap[0])

def move(xpos, ypos, direction, lmap):
    match direction.lower():
        case "n":
            ypos -= 1
        case "s":
            ypos += 1
        case "e":
            xpos -= 1
        case "w":
            xpos += 1
    newx, newy= xpos, ypos


    if not in_bounds(newx, newy, lmap):
        return xpos, ypos, lmap[ypos-1][xpos], False, "out of bounds"

    destination = lmap[newy][newx]
    if destination == "x":
        return xpos, ypos, lmap[ypos][xpos], False, "a wall blocks you"


    return newx, newy, destination, True, f'\nyou moved to the {destination.replace("_", " ")}\n'



def generate_map():
    temp = [
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","Castle interior","castle","street","street", "Market (healing items)","Market interior","x","Final boss","x"],
            ["x","Castle courtyard","x","x","street","x","x","x","Barrier (LV requirement)","x"],
            ["x","Castle tower","x","Training area","street", "Armoury (weapons and armour)","Armoury interior","x","street","x"],
            ["x","x","x","x","street","x","x","x","street","Exit (requires key held by final boss)"],
            ["x","Secret item","street","street","street", "Potion shop (temporary buffs)","Potion shop interior","x","street","x"],
            ["x","x","x","x","street","x","x","street","street","x"],
            ["x","Mini boss","Barrier (LV requirement)","street","street","street","barrier (requires mini-boss dead)","street","Forest (hard exp gain)","x"],
            ["x","x","x","x", "Gladiator arena (challenges + medium exp gain)","x","x","x","x","x"],
            ["x","Secret Shop interior","secret shop","street","street","x","x","x","x","x"],
           ]

    return temp

def interact(player,xpos,ypos,lmap,interaction,inv):
    if lmap[ypos][xpos] == "Castle interior":
        if not interaction:
            print(f"the king looks at you with an expectant look")
            t.sleep(1)
            print(f"'go on then! I don't have much time for you.' he yells")
            t.sleep(1)
            print(f"waving his had to dismiss you.")
            return True, inv
        else:
            print(f"the king refuses to talk to you again")
            t.sleep(1)
            return True, inv



    elif lmap[ypos][xpos] == "Castle courtyard":
        if not interaction:
            print(f"there is a fountain in the middle of the yard")
            t.sleep(1)
            print(f"you look inside to see the pennies of many people wishing")
            t.sleep(1)
            if input(f"Take some? (y/n): ").lower() == "y":
                inv["gold"] += 50
                print(f"You take 50 coins from the well")
                t.sleep(1)
                print(f"You have a bad feeling about doing that.")
                t.sleep(1)
                print(f"you now have {inv["gold"]} gold")
                t.sleep(1)
                print(f"you walk away from the fountain.")
                fountain_interaction = True
            else:
                pass
        else:
            print(f"You've already looked around")

    elif lmap[ypos][xpos] == "Castle tower":
        if not interaction:
            print(f"around you is a dark, dingy room. riddled with cobwebs and dust")
            t.sleep(1)
            print(f"you look around and see a shadowy chest in the corner, emitting an ominous aura")
            t.sleep(1)
            if input(f"open the chest?(y/n): ").lower() == "y":
                print(f"you open the chest to find heaps of gold")
                t.sleep(1)
                print(f"you gained 500 gold")
                inv["gold"] += 500
                t.sleep(1)
                print(f"you keep looking in the chest, and you find an ominous looking dagger")
                t.sleep(1)
                player.weapon = shadow_dagger
                print(f"you have equipped the {player.weapon.name}")
            else:
                print(f"you leave the chest in the corner")

def main():
    #setups
    player = Player(level=1, name="Player", hp=100, armour=nothing, weapon= wood_sword, position=[0][0])
    locked_weapons = [iron_sword, obsidian_sword, shadow_sword, shadow_dagger]
    unlocked_weapons = [wood_sword]
    inventory = {
        "gold": 0,
        "weapon": player.weapon.name,
        "armour": player.armour.name,
        "apples": 0
    }

    local_map = generate_map()

    y_pos, x_pos = 1, 1
    player.position = local_map[y_pos][x_pos]

    # action variables
    moved = False
    interacted = False
    attacked = False
    checked = False
    tut_won = False
    fountain_interaction = False # SO PEOPLE CAN'T INF GRIND MONEY
    tower_interaction = False # ONLY OPEN SECRET CHEST ONCE


    print(f"the king explains what you must do")
    t.sleep(1)
    print(f"'you must defeat the (mini-boss) and then defeat the (final boss) in order to win'")
    t.sleep(5)
    print(f"'and to do that, i must show you how to fight.'")
    t.sleep(2)
    print(f"he hands you 2 apples, they seem to regenerate health")
    inventory["apples"] += 2
    t.sleep(2)
    print(f"A training dummy rises from the floor")
    t.sleep(2)

    while not tut_won:
        tut_won = tutorial_fight_sequence(player)
        if tut_won:
            print(f"The king congratulates you on your victory")
            t.sleep(1)
            print(f"'well done, you now understand the basics of combat'")
            t.sleep(1)
            print(f"'good luck on your journey'")
            t.sleep(1)
            break
        else:
            print(f"The king sighs in disappointment")
            t.sleep(1)
            print(f"'lets try that again, shall we?'")



    print(f'you are currently in the {player.position.replace("_", " ")}\n')
    while True:
        action = int(input("1) Move\n2) Interact/look around\n3) Attack\n4) Check self/inventory\nwhat do you want to do?: "))

        #MOVEMENT
        if action == 1:
            if local_map[y_pos-1][x_pos] != "x":
                print(f"\nNorth of you is the {local_map[y_pos-1][x_pos]}")

            if local_map[y_pos+1][x_pos] != "x":
                print(f"\nSouth of you is the {local_map[y_pos+1][x_pos]}")

            if local_map[y_pos][x_pos+1] != "x":
                print(f"\nWest of you is the {local_map[y_pos][x_pos+1]}")

            if local_map[y_pos][x_pos-1] != "x":
                print(f"\nEast of you is the {local_map[y_pos][x_pos-1]}")

            direction = input("where do you want to go (using n/s/e/w): ")
            new_x, new_y, tile, moved, msg = move(x_pos, y_pos, direction, local_map)
            print(msg)

        elif action == 2:
            interacted, inventory = interact(player, x_pos, y_pos, local_map, interacted, inventory)

        elif action == 3:
            '''PLACEHOLDER'''

        elif action == 4:
            print(f"health: {player.hp}/{player.maxhealth}")
            for keys, values in inventory.items():
                print(f"{keys}: {values}\n")

        if moved:
            interacted = False
            prev_y, prev_x = y_pos, x_pos
            y_pos, x_pos  = new_y, new_x
            player.position = tile

            if player.position == local_map[3][3]: # checks if on the training arena
                print(f"you stand outside of a training arena.")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    fight_win = training_fight_sequence(player)
                    if fight_win:
                        print(f"you walk away from the arena.")
                        player.position = local_map[prev_y][prev_x]
                    else:
                        print(f"better luck next time!")
                        t.sleep(1)
                        print(f"you walk away from the arena.")
                        player.position = local_map[prev_y][prev_x]


                elif input("go inside?(y/n): ").lower() == "n":
                    print(f"you walk away from the arena.")
                    player.position = local_map[prev_y][prev_x]









if __name__ == "__main__":
    main()