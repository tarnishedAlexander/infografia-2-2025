from abc import ABC, abstractmethod
import random

class Character(ABC):
    def __init__(self, health, base_attack, defense, probCrit, probAbility=0.2):
        self.health = health
        self.base_attack = base_attack  
        self.defense = defense
        self.probCrit = probCrit
        self.probAbility = probAbility  
    
    def attack(self, other):
        damage = self.base_attack - other.defense  
        if damage < 0:
            damage = 0
        if random.random() < self.probCrit:
            damage *= 2
            print(f"{type(self).__name__} lands a critical hit!")
        other.take_damage(damage)
        
        if random.random() < self.probAbility:
            self.ability()
            print(f"{type(self).__name__} used an ability!")
    
    def take_damage(self, damage): 
        self.health -= damage
        if self.health < 0:
            self.health = 0

    @abstractmethod
    def ability(self):
        pass    
    
    def get_health(self): 
        return self.health
    
    def get_attack(self): 
        return self.base_attack  
    
    def get_defense(self):  
        return self.defense