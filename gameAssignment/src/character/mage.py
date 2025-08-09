from character.character import Character

class Mage(Character):
    def __init__(self, health, base_attack, defense, probCrit, probAbility=0.2):
        super().__init__(health, base_attack, defense, probCrit, probAbility)

    def ability(self):
        self.base_attack *= 2
        print(f"El mago lanzo el onshot ability Comet Azur {self.base_attack} de daño")
