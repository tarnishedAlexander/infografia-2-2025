from character.character import Character

class Hero(Character):
    def __init__(self, health, base_attack, defense, probCrit):
        super().__init__(health, base_attack, defense, probCrit)
        self.ability_name = "Delizadeza del sabueso"
        self.ability_damage = 30

    def ability(self):
        print(f"El héroe lanza su habilidad {self.ability_name} causando {self.ability_damage} de daño")
        