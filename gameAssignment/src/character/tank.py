from character.character import Character

class Tank(Character):
    def __init__(self, health, base_attack, defense, probCrit, probAbility=0.2):
        super().__init__(health, base_attack, defense, probCrit, probAbility)

    def ability(self):
        self.defense *= 2
        print(f"El tanque uso un poderoso hechizo que le da un buff tremendo a su defensa el \"Golden Vow\", ahora tiene {self.defense} de defensa")