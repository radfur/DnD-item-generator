import random
from armor import armor
from weapon import weapon
from weapon_generator import *
import json

file_path = "src\data.json"

with open(file_path, "r") as file:
    data = json.load(file)

weapon_names = data["weapon_names"]

random_weapon_name = random.choice(weapon_names)

weapon = weapon(random_weapon_name, None, None)
#weapon.generate_damage_type()
weapon.damage_range()

print(weapon.description())
