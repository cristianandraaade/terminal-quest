from entities.character import Character
import random

class Enemy(Character):
    def __init__(self):
        self.__enemy = self.get_Type_Enemy()
        if self.__enemy == "Goblin":
            life,attack,defense = 50,50,50
        if self.__enemy == "Troll":
            life, attack, defense = 90,40,80
        if self.__enemy == "Orc":
            life, attack, defense = 40,90,30
        super().__init__(life, attack, defense)

    def get_Type_Enemy(self)->str:
        enemies = ["Goblin", "Troll", "Orc"]
        return random.choice(enemies)
    
    def get_enemy(self)->str:
        return self.__enemy
    def __str__(self)->str:
        return f"Inimigo: {self.__enemy} | Vida: {self.get_Life()} | Ataque: {self.get_Attack()} | Defesa: {self.get_Defense()}"
    
    def get_DisplayName(self):
        return f"{self.get_enemy()}"
