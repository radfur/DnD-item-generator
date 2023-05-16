class armor:
    def __init__(self, name, resistance, armor_class):
        self.name = name
        self.resistance = resistance
        self.armor_class = armor_class
    
    def description(self):
        return f"{self.name} - "