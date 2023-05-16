import random
from armor import armor
from weapon import weapon
#from item import item
from data import *

random_weapon_name = random.choice(weapon_names)

weapon = weapon(random_weapon_name, None, None)
#weapon.generate_damage_type()
weapon.damage_range()

print(weapon.description())
weapon.damage_range()
print(weapon.description())