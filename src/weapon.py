import random
from data import *

class weapon:
    def __init__(self, name, damage_type, damage):
        self.name = name
        self.damage_type = damage_type
        self.damage = damage
        
    def description(self):
        return f"{self.name} - deals damage type {self.damage_type} equal to {self.damage} + proficiency mod and stat mod"
    
    def damage_range(self):
        if self.name == "Sword":
            unique_damage = ["1d8", "1d6"]
            self.damage = random.choice(unique_damage)
        else:
            self.damage_type = random.choice(damage)