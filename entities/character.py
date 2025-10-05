class Character:
    def __init__(self, life, attack, defense):

        self.__life = life
        self.__attack = attack
        self.__defense = defense
        self.__level = 1

    def get_Life(self) -> str:
        return self.__life

    def set_Life(self, life: str) -> None:
        self.__life = life

    def get_Attack(self) -> str:
        return self.__attack

    def set_Attack(self, attack: str) -> None:
        self.__attack = attack

    def get_Defense(self) -> str:
        return self.__defense

    def set_Defense(self, defense: str) -> None:
        self.__defense = defense

    def make_attack(self, target):
        damage = self.__attack - (target.get_Defense() * 0.5)
        if damage < 0:
            damage = 0
        target.take_damage(damage)
        print(f"{self.get_DisplayName()} causa {damage} de dano em {target.get_DisplayName()}!\n")
        
    def take_damage(self, damage):
        self.__life -=damage
        
    def get_DisplayName():
        return