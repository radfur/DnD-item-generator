import random
import json

file_path = "src\data.json"

with open(file_path, "r") as file:
    data = json.load(file)

damage = data["damage"]

def damage_range(self):
        if self.name == "Sword":
            unique_damage = ["1d8", "1d6"]
            self.damage = random.choice(unique_damage)
        else:
            self.damage_type = random.choice(damage)