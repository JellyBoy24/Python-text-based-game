from Game.Fights.training import training_fight_sequence
from Game.main import Player
from Game.objects import *
player = Player(level=1, name="Player", hp=100, armour=nothing, weapon= wood_sword, position=[0][0])
training_fight_sequence(player)
