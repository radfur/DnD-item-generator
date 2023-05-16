import random
import json

file_path = "src\data.json"

with open(file_path, "r") as file:
    data = json.load(file)

class weapon:
    def __init__(self, name, damage_type, damage):
        self.name = name
        self.damage_type = damage_type
        self.damage = damage
        
    def description(self):
        return f"{self.name} - deals damage type {self.damage_type} equal to {self.damage} + proficiency mod and stat mod"
    
    