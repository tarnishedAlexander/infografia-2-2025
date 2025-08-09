from character.character import Character

class Samurai(Character):
    def __init__(self, health, base_attack, defense, probCrit, probAbility=0.2):
        super().__init__(health, base_attack, defense, probCrit, probAbility)
        self.ability_name = "Rios de sangre"
        self.ability_damage = 50

    def ability(self):
        print(f"El samurai lanza su habilidad {self.ability_name} causando sangrado de {self.ability_damage} de daño")
