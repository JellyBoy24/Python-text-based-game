from Game.Shops.potion import potion_shop_sequence
from Game.main import Player
from Game.objects import *


player = Player(level=1, name="Player", hp=100, armour=iron, weapon= obsidian_sword, position=[0][0])
inventory = {
        "gold": 5000,
        "apples": 5,
        "heal_potions": 0,
        "large_heal_potions": 0,
        "full_heal": 9
    }
inventory = potion_shop_sequence(player,inventory, False)



