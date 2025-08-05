import random
class Character:
    def __init__(
        self, 
        hp: int, 
        base_damage: int, 
        parry_prob: float, 
        crit_prob: float
    ):
        self.hp = hp
        self.base_damage = base_damage
        self.parry_prob = parry_prob
        self.crit_prob = crit_prob
        self.name = "default"
    
    def attack(self, other):
        damage = self.base_damage * 2 if random.random()<=self.crit_prob else self.base_damage
        print(f"atacando a {other} con {damage} daño")
        other.hurt(damage)

    def hurt(self, damage: int):
        damage_taken = 0 if random.random()<=self.parry_prob else damage
        self.hp -= damage_taken
        print(f"ouch! recibido daño de {damage_taken}, hp restante: {self.hp}")
    
    def set_name(self, name):
        self.name = name
    
        
        