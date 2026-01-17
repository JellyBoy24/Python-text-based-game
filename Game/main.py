from Game.Fights.alley import alley_fight_sequence
from Game.Shops.market import market_shop_sequence
from Game.Shops.armoury import armoury_shop_sequence
from Game.Fights.training import training_fight_sequence
from Game.Fights.arena import arena_fight_sequence
from Game.Fights.tutorial import tutorial_fight_sequence
from Game.Fights.forest import forest_fight_sequence
from Game.Shops.potion import potion_shop_sequence
from Game.Fights.miniboss import mini_boss_fight_sequence
from Game.Fights.bossfight import boss_fight_sequence
from Game.Shops.secret import secret_shop_sequence
from Game.objects import *
from Game.entities import Entity
import time as t


class Player(Entity):
    def __init__(self, level, name, hp: int, armour: Armour, weapon: Weapon, position):
        self.position = position
        super().__init__(level, name, hp, armour, weapon)


def in_bounds(x, y, lmap):
    return 0 <= y < len(lmap) and 0 <= x < len(lmap[0])

def move(xpos, ypos, direction, lmap, mboss_dead, fboss_dead):
    match direction.lower():
        case "w":
            ypos -= 1
        case "s":
            ypos += 1
        case "a":
            xpos -= 1
        case "d":
            xpos += 1
    newx, newy= xpos, ypos


    if not in_bounds(newx, newy, lmap):
        return xpos, ypos, lmap[ypos-1][xpos], False, "out of bounds"

    destination = lmap[newy][newx]
    if destination == "x":
        return xpos, ypos, lmap[ypos][xpos], False, "a wall blocks you"

    elif destination.startswith("barrier"):
        if not mboss_dead:
            return xpos, ypos, lmap[ypos][xpos], False, "a barrier blocks you, seems you must defeat a smaller boss first, go west"
        else:
            return newx, newy, destination, True, f'\nyou moved to the {destination.replace("_", " ")}\n'
    elif destination.startswith("Exit"):
        if not fboss_dead:
            return xpos, ypos, lmap[ypos][xpos], False, "a barrier blocks you, seems you must defeat the final boss first, go north"
        else:
            return newx, newy, destination, True, f'\nyou moved to the {destination.replace("_", " ")}\n'
    return newx, newy, destination, True, f'\nyou moved to the {destination.replace("_", " ")}\n'



def generate_map():
    temp = [
            ["x","x","x","x","x","x","x","x","x","x"],
            ["x","Castle interior","castle entrance","street","street", "Market (healing apples)","Market interior","x","Final boss","x"],
            ["x","Castle courtyard","x","x","street","x","x","x","street","x"],
            ["x","Castle tower","x","Training area","street", "Armoury (weapons and armour)","Armoury interior","x","street","x"],
            ["x","x","x","x","street","x","x","x","street","Exit"],
            ["x","alleys","alley","alley","street", "Potion shop (healing potions)","Potion shop interior","x","street","x"],
            ["x","x","x","x","street","x","x","street","street","x"],
            ["x","Mini boss","street","street","street","street","barrier (requires mini-boss dead)","street","Forest","x"],
            ["x","x","x","x", "Gladiator arena","street","x","x","x","x"],
            ["x","Secret Shop interior","secret shop","street","street","street","x","x","x","x"],
            ["x","x","x","x","x","x","x","x","x","x"]
           ]

    return temp


def main():
    #setups
    player = Player(level=1, name="Player", hp=100, armour=nothing, weapon=wood_sword, position=[0][0])
    locked_weapons = [copper_sword, iron_sword]
    locked_armour = [leather, chainmail, iron]
    unlocked_weapons = [wood_sword]
    unlocked_armour = [nothing]
    inventory = {
        "gold": 0,
        "weapon": player.weapon.name,
        "armour": player.armour.name,
        "apples": 0,
        "heal_potions": 0,
        "large_heal_potions": 0,
        "full_heal": 0
    }

    local_map = generate_map()

    y_pos, x_pos = 1, 1
    player.position = local_map[y_pos][x_pos]

    # action variables
    moved = False
    interacted = False
    attacked = False
    tutorial = False
    tut_apples = False
    tut_won = False
    alley_won = False
    fountain_interaction = False # SO PEOPLE CAN'T INF GRIND MONEY
    fountain_attack = False # SAME AS FOUNTAIN
    tower_interaction = False # ONLY OPEN SECRET CHEST ONCE
    tower_attack = False
    alley_interaction = False # SO NO MULTIPLE SETS OF ARMOUR/SWORDS
    market_keeper_dead = False
    armoury_keeper_dead = False
    potion_keeper_dead = False
    secret_keeper_dead = False
    mini_boss_dead = False
    final_boss_dead = False

    while not tutorial:
        print(f"the king explains what you must do")
        t.sleep(1)
        print(f"'you must defeat the (mini-boss) and then defeat the (final boss) in order to win'")
        t.sleep(5)
        print(f"'and to do that, i must show you how to fight.'")
        t.sleep(2)
        print("there can be up to 3 enemies in combat at once")
        t.sleep(2)
        print("attack will deal your weapons damage to the enemy/target")
        t.sleep(2)
        print("defend will reduce the first hit of damage you take by 50%")
        t.sleep(3)
        print("skill uses the skill of your weapons, be warned, the skill can fail")
        t.sleep(3)
        print(f"the king hands you 2 apples")
        if not tut_apples:
            inventory["apples"] += 2
            tut_apples = True
        else:
            print("the king reminds you of the 2 apples he gave you")
        t.sleep(2)
        print("eat those to regain health, all healing items will be in the items option\n"
              "low heal (apples) = 5 hp\n"
              "medium heal (heal potions) = 25 hp\n"
              "high heal (large heal potions) = 50 hp\n"
              "full heal (full heals) = 100 hp")
        t.sleep(5)
        print("inspect means to check the enemies/targets health, damage, skills, and armour")
        t.sleep(3)
        if input("'ready?' the king asks patiently(y/n): ").lower() == "y":
            break
        else:
            print("lets go over that again")
    print(f"A training dummy rises from the floor")
    t.sleep(2)

    while not tut_won:
        tut_won = tutorial_fight_sequence(player, inventory)
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
            t.sleep(2)



    print(f'you are currently in the {player.position.replace("_", " ")}\n')
    while True:
        try:
            action = int(input("1) Move\n2) Interact/look around\n3) Attack\n4) Check self/inventory\nwhat do you want to do?: "))
        except ValueError:
            print("not an option")
            continue
        else:
            if action not in [1, 2, 3, 4]:
                print("not an option")
                continue

        #MOVEMENT
        if action == 1:
            if local_map[y_pos-1][x_pos] != "x":
                print(f"\nNorth of you is the {local_map[y_pos-1][x_pos]}")

            if local_map[y_pos+1][x_pos] != "x":
                print(f"\nSouth of you is the {local_map[y_pos+1][x_pos]}")

            if local_map[y_pos][x_pos+1] != "x":
                print(f"\nEast of you is the {local_map[y_pos][x_pos+1]}")

            if local_map[y_pos][x_pos-1] != "x":
                print(f"\nWest of you is the {local_map[y_pos][x_pos-1]}")

            direction = input("where do you want to go (using w/a/s/d): ").lower()
            new_x, new_y, tile, moved, msg = move(x_pos, y_pos, direction, local_map, mini_boss_dead, final_boss_dead)
            print(msg)

        elif action == 2:
            if local_map[y_pos][x_pos] == "street":
                print("you cant do that on the street")
                continue

            elif local_map[y_pos][x_pos] == "Castle interior":
                if not interacted:
                    print(f"the king looks at you with an expectant look")
                    t.sleep(1)
                    print(f"'go on then! I don't have much time for you.' he yells")
                    t.sleep(1)
                    print(f"waving his had to dismiss you.")
                    interacted = True
                else:
                    print(f"the king refuses to talk to you again")
                    t.sleep(1)

            elif local_map[y_pos][x_pos] == "Castle courtyard":
                if not interacted and not fountain_interaction:
                    print(f"there is a fountain in the middle of the yard")
                    t.sleep(1)
                    print(f"you look inside to see the pennies of many people wishing")
                    t.sleep(1)
                    if input(f"Take some? (y/n): ").lower() == "y":
                        inventory["gold"] += 50
                        print(f"You take 50 coins from the well")
                        t.sleep(1)
                        print(f"You have a bad feeling about doing that.")
                        t.sleep(1)
                        print(f"you now have {inventory['gold']} gold")
                        t.sleep(1)
                        print(f"you walk away from the fountain.")
                        interacted = True
                        fountain_interaction = True
                    else:
                        pass
                else:
                    print(f"You've already looked around")

            elif local_map[y_pos][x_pos] == "Castle tower":
                if not interacted and not tower_interaction:
                    print(f"around you is a dark, dingy room. riddled with cobwebs and dust")
                    t.sleep(1)
                    print(f"you look around and see a shadowy chest in the corner, emitting an ominous aura")
                    t.sleep(1)
                    if input(f"open the chest?(y/n): ").lower() == "y":
                        print(f"you open the chest to find heaps of gold")
                        t.sleep(1)
                        print(f"you gained 500 gold")
                        inventory["gold"] += 500
                        t.sleep(1)
                        print(f"you keep looking in the chest, and you find an ominous looking dagger")
                        t.sleep(1)
                        player.weapon = shadow_dagger
                        inventory["weapon"] = player.weapon.name
                        print(f"you have equipped the {player.weapon.name}")
                        interacted = True
                        tower_interaction = True
                    else:
                        print(f"you leave the chest in the corner")

            elif local_map[y_pos][x_pos] == "alleys":
                if not interacted and not alley_interaction:
                    print("you rummage through the garbage pile")
                    t.sleep(2)
                    print("the stench is horrendous")
                    t.sleep(1)
                    print("you feel something hard and sturdy")
                    t.sleep(2)
                    print("you pick it up to see some obsidian armour and an obsidian sword")
                    t.sleep(3)
                    if input(f"take them?(y/n): ").lower() == "y":
                        player.weapon = obsidian_sword
                        player.armour = obsidian
                        unlocked_weapons.append(obsidian_sword)
                        unlocked_armour.append(obsidian)
                        alley_interaction = True
                    else:
                        print(f"You put them down, you remember you can always come back")
                        t.sleep(2)
                        continue
                    interacted = True
                else:
                    print(f"You've already looked around")
                    t.sleep(1)
                    continue

        elif action == 3:
            if local_map[y_pos][x_pos] == "street":
                print("you cant do that on the street")
                continue

            elif local_map[y_pos][x_pos] == "Castle interior":
                if not attacked:
                    print(f"a sudden force stops you")
                    t.sleep(1)
                    print(f"the king smirks at you knowingly")
                    t.sleep(1)
                    print("'good luck on your journey'")
                    attacked = True
                else:
                    print(f"force stops you before you even try")
                    t.sleep(1)

            elif local_map[y_pos][x_pos] == "Castle courtyard":
                if not attacked and not fountain_attack:
                    print(f"you attack the fountain in the middle")
                    t.sleep(1)
                    print(f"water leaks out of it")
                    t.sleep(1)
                    print("some gold spills from it")
                    if input(f"Take some? (y/n): ").lower() == "y":
                        inventory["gold"] += 50
                        print(f"You take 50 coins from the now destroyed fountain")
                        t.sleep(1)
                        print(f"You have a bad feeling about doing that.")
                        t.sleep(1)
                        print(f"you now have {inventory['gold']} gold")
                        t.sleep(1)
                        print(f"you walk away from the destroyed fountain.")
                        attacked = True
                    else:
                        pass
                else:
                    print(f"You've already destroyed it")

            elif local_map[y_pos][x_pos] == "Castle tower":
                if not attacked and not tower_attack:
                    print(f"you look around the towers dark room")
                    t.sleep(1)
                    print(f"you swing your sword violently at everything until it hits an ominous looking chest")
                    t.sleep(1)
                    if input(f"open the chest?(y/n): ").lower() == "y":
                        print(f"you open the chest to find heaps of gold")
                        t.sleep(1)
                        print(f"you gained 500 gold")
                        inventory["gold"] += 500
                        t.sleep(1)
                        print(f"you keep looking in the chest, and you find an ominous looking dagger")
                        t.sleep(1)
                        player.weapon = shadow_dagger
                        inventory["weapon"] = player.weapon.name
                        print(f"you have equipped the {player.weapon.name}")
                        interacted = True
                        tower_interaction = True
                    else:
                        print(f"you hit the chest once more before leaving it")

            elif local_map[y_pos][x_pos] == "alleys":
                if not attacked and not alley_interaction:
                    print("you hit the garbage pile")
                    t.sleep(1)
                    print("the stench is horrendous")
                    t.sleep(1)
                    print("your sword hit something solid and sturdy")
                    t.sleep(2)
                    print("you pick up the object to see some obsidian armour and a sword")
                    t.sleep(3)
                    if input(f"take them?(y/n): ").lower() == "y":
                        player.weapon = obsidian_sword
                        player.armour = obsidian
                        unlocked_weapons.append(obsidian_sword)
                        unlocked_armour.append(obsidian)
                        alley_interaction = True
                    else:
                        print(f"You put them down, you remember you can always come back")
                        t.sleep(2)
                        continue
                    interacted = True
                else:
                    print(f"You've already attacked the pile")
                    t.sleep(1)
                    continue

        elif action == 4:
            print(f"\nhealth: {player.hp}/{player.maxhealth}\n")
            for keys, values in inventory.items():
                if keys == "weapon":
                    print(f"weapon: {player.weapon.name}")
                    continue
                elif keys == "armour":
                    print(f"armour: {player.armour.name}")
                    continue
                print(f"{keys}: {values}")
            print("0) exit\n1) change weapon\n2) view weapon stats\n3) change armour\n4) view armour stats\n")
            t.sleep(1)
            inventory_choice = int(input("what do you want to do? (0/1/2/3/4): "))
            if inventory_choice == 0:
                continue

            elif inventory_choice == 1:
                for items in unlocked_weapons:
                    print(items.name)
                    t.sleep(0.3)
                weapon_switch = int(input("which weapon do you want to equip?(1,2,3 ETC): "))
                if weapon_switch == 0:
                    print("you cant do that")
                else:
                    if not (weapon_switch > len(unlocked_weapons)):
                        if player.weapon not in unlocked_weapons:
                            unlocked_weapons.append(player.weapon) # saves the last weapon equipped
                        player.weapon = unlocked_weapons[weapon_switch - 1]
                        print(f"you equipped the {player.weapon.name}")
                        inventory["weapon"] = player.weapon
                    else:
                        print("you cant pick that")

            elif inventory_choice == 2:
                print(player.weapon.name)
                t.sleep(0.3)
                print(f"it deals {player.weapon.damage} damage")
                t.sleep(0.3)
                print(f"it can use a skill called {player.weapon.skill_name} that deals {player.weapon.skill_dmg} damage")
                t.sleep(0.3)
                print(f"the chance of it using the skill is {player.weapon.skill_chance * 100}%")
                t.sleep(0.3)

            elif inventory_choice == 3:
                for items in unlocked_armour:
                    print(items.name)
                    t.sleep(0.3)
                armour_switch = int(input("which armour do you want to equip?(1,2,3 ETC): "))
                if armour_switch == 0:
                    print("you cant do that")
                else:
                    if not armour_switch > len(unlocked_armour):
                        if player.armour not in unlocked_armour:
                            unlocked_armour.append(player.armour)  # saves the last warmour equipped
                        player.armour = unlocked_weapons[armour_switch - 1]
                        print(f"you equipped the {player.armour.name} armour")
                        inventory["armour"] = player.armour
                    else:
                        print("you cant pick that")

            elif inventory_choice == 4:
                print(player.armour.name)
                t.sleep(0.3)
                print(f"it reduces damage by {player.armour.defence*100}%")
                t.sleep(0.3)


        if moved:
            interacted = False
            attacked = False
            y_pos, x_pos  = new_y, new_x
            player.position = tile



            if player.position == local_map[1][2]: # checks if on castle entrance
                print(f"you stand outside of a castle")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    player.position = local_map[1][1]
                    y_pos, x_pos = 1, 1
                    print(f"you went inside the castle")
                else:
                    player.position = local_map[1][3]
                    y_pos, x_pos = 1, 3
                    print(f"you walk away from the castle into the street.")
                    print(player.position)

            elif player.position == local_map[1][5]: # check if on the market
                print(f"you stand outside of a busy market")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    player.position = local_map[1][6]
                    y_pos, x_pos = 1, 6
                    print(f"you went inside the market")
                    inventory, market_keeper_dead = market_shop_sequence(player, inventory, market_keeper_dead)
                    player.hp = 100
                    print("you walk away from the market.")
                    t.sleep(1)
                    player.position = local_map[1][4]
                    y_pos, x_pos = 1, 4
                else:
                    player.position = local_map[1][4]
                    y_pos, x_pos = 1, 4
                    print("you walk away from the market.")


            elif player.position == local_map[3][5]: # checks if on the armoury
                print(f"you stand outside of an armoury")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    player.position = local_map[3][6]
                    y_pos, x_pos = 3, 6
                    print(f"you walk inside the armoury")
                    inventory, armoury_keeper_dead, sword, shielda = armoury_shop_sequence(player, inventory, locked_weapons, locked_armour, armoury_keeper_dead)
                    player.hp = 100
                    print("you walk away from the armoury.")
                    if sword is not None:
                        unlocked_weapons.append(sword)
                        if sword in locked_weapons:
                            locked_weapons.remove(sword)
                    if shielda is not None:
                        unlocked_armour.append(shielda)
                        if shielda in locked_armour:
                            locked_armour.remove(shielda)
                    t.sleep(1)
                    player.position = local_map[3][4]
                    y_pos, x_pos = 3, 5
                else:
                    player.position = local_map[3][4]
                    y_pos, x_pos = 3, 5
                    print("you walk away from the armoury.")

            elif player.position == local_map[5][5]: # checks if on the potion shop
                print(f"you stand outside of a potion makers hut")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    player.position = local_map[5][6]
                    y_pos, x_pos = 5, 6
                    print("you walk inside, hearing the bubbling of boiling water")
                    inventory, potion_keeper_dead = potion_shop_sequence(player, inventory, potion_keeper_dead)
                    player.hp = 100
                    print("you walk away from the hut.")
                    player.position = local_map[5][4]
                    y_pos, x_pos = 5, 5
                else:
                    player.position = local_map[5][4]
                    y_pos, x_pos = 5, 5
                    print("you walk away from the hut.")

            elif player.position == local_map[5][2]: # checks if player is on the second alleyway
                if not alley_won:
                    print(f"as you walk down the alleyway, you see a shadowy figure move in the back")
                    if input("continue?(y/n): ").lower() == "y":
                        fight_win, inventory = alley_fight_sequence(player, inventory)
                        player.hp = 100
                        if fight_win:
                            alley_won = True
                            print("they fled and dropped 250 gold")
                            inventory["gold"] += 250
                        else:
                            print("they shove you out of the alleyway")
                            player.position = local_map[5][4]
                    else:
                        print("you walk away from the alleyway")
                        player.position = local_map[5][4]
                else:
                    continue

            elif player.position == local_map[5][1]: # checks if on the secret item
                print("you come across a pile of garbage on the floor")
                t.sleep(1)
                print("it reeks")

            elif player.position == local_map[7][1]: # checks if on the mini boss
                print("you come across a small woodland area")
                if input("enter?(y/n): ").lower() == "y":
                    print("a giant orc appears from behind a tree")
                    t.sleep(1)
                    fight_win, inventory = mini_boss_fight_sequence(player, inventory)
                    player.hp = 100
                    if fight_win:
                        print("the orc falls dead, you sense a barrier fade away")
                        mini_boss_dead = True
                        inventory["gold"] += 2500
                    else:
                        print("the orc kicks you out of the forest")
                        t.sleep(1)
                        player.position = local_map[7][2]
                        y_pos, x_pos = 7, 2

            elif player.position == local_map[1][8]: # checks if on final boss
                print("you see a small cave area")
                t.sleep(1)
                if input("enter?(y/n): ").lower() == "y":
                    print("inside it is way larger than you think")
                    t.sleep(2)
                    print("as you step forward, you hear a low growl from the back of the cave")
                    t.sleep(2)
                    print("a large dragon emerges from the shadows of the cave")
                    t.sleep(2)
                    if market_keeper_dead and armoury_keeper_dead and potion_keeper_dead and secret_keeper_dead and mini_boss_dead:
                        print("apon seeing you, the dragons eyes widen with fear")
                        t.sleep(1)
                        print("he knows what you have done")
                        t.sleep(2)
                        print("he stabs himself in the throat with his own claw, taking his own life before you can")
                        fight_win = True
                    else:
                        fight_win, inventory = boss_fight_sequence(player, inventory)
                        player.hp = 100

                    if fight_win:
                        print("the final boss has fallen, a barrier seems to fade in the distance")
                        t.sleep(1)
                        print("you have gained the scales of the dragon as a wearable armour")
                        unlocked_armour.append(scales)
                        inventory["gold"] += 5000
                        t.sleep(1)
                    else:
                        print("the dragon's fire pushes you out of the cave")

                else:
                    print("you walk away from the cave")
                    player.position = local_map[2][8]
                    y_pos, x_pos = 2, 8


            elif player.position == local_map[9][2]: # checks if on the secret shop
                print(f"you stand outside of a dark, cloaked box")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    player.position = local_map[9][1]
                    y_pos, x_pos = 9, 1
                    print("you walk inside, hearing the whoosh of wind")
                    inventory, secret_keeper_dead, sword, shielda = secret_shop_sequence(player, inventory,secret_keeper_dead)
                    player.hp = 100
                    print("you walk away from the cloaked box.")
                    if sword is not None:
                        unlocked_weapons.append(sword)
                        if sword in locked_weapons:
                            locked_weapons.remove(sword)
                    if shielda is not None:
                        unlocked_armour.append(shielda)
                        if shielda in locked_armour:
                            locked_armour.remove(shielda)
                    player.position = local_map[9][3]
                    y_pos, x_pos = 9, 3
                else:
                    player.position = local_map[9][3]
                    y_pos, x_pos = 9, 3
                    print("you walk away from the cloaked box.")

            elif player.position == local_map[3][3]: # checks if on the training arena
                print(f"you stand outside of a training arena.")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    fight_win, inventory = training_fight_sequence(player, inventory)
                    player.hp = 100
                    if fight_win:
                        inventory["gold"] += 500
                        print(f"you walk away from the arena.")
                        player.position = local_map[3][4]
                        y_pos, x_pos = 3, 4
                    else:
                        print(f"better luck next time!")
                        t.sleep(1)
                        print(f"you walk away from the arena.")
                        player.position = local_map[3][4]
                        y_pos, x_pos = 3, 4
                else:
                    print("you walk away from the arena.")
                    player.position = local_map[3][4]
                    y_pos, x_pos = 3, 4



            elif player.position == local_map[8][4]: # checks if on the arena
                print(f"you stand outside of a gladiators arena.")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    fight_win, inventory = arena_fight_sequence(player, inventory)
                    player.hp = 100
                    if fight_win:
                        inventory["gold"] += 1000
                        print(f"you walk away from the arena.")
                        player.position = local_map[7][4]
                        y_pos, x_pos = 7, 4
                    else:
                        print(f"better luck next time!")
                        t.sleep(1)
                        print(f"you walk away from the arena.")
                        player.position = local_map[7][4]
                        y_pos, x_pos = 7, 4
                else:
                    print("you walk away from the arena.")
                    player.position = local_map[7][4]
                    y_pos, x_pos = 7, 4

            elif player.position == local_map[7][8]: # checks if on the forest
                print(f"you stand outside of a forest.")
                t.sleep(1)
                if input("go inside?(y/n): ").lower() == "y":
                    fight_win, inventory = forest_fight_sequence(player, inventory)
                    player.hp = 100
                    if fight_win:
                        inventory["gold"] += 2000
                        print(f"you walk away from the forest.")
                        player.position = local_map[7][7]
                        y_pos, x_pos = 7, 7
                    else:
                        print(f"better luck next time!")
                        t.sleep(1)
                        print(f"you walk away from the forest.")
                        player.position = local_map[7][7]
                        y_pos, x_pos = 7, 7
                else:
                    print("you walk away from the forest.")
                    player.position = local_map[7][7]
                    y_pos, x_pos = 7, 7

            elif player.position == local_map[4][9]: #checks if on the exit
                print("congratulations!")
                t.sleep(1)
                print(f"you win!")
                t.sleep(1)
                exit()



if __name__ == "__main__":
    main()