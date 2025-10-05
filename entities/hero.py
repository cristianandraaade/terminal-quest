from entities.character import Character


class Hero(Character):
    """Atributos iniciais do heroi
        vida = 70pontos
        attack= 60 pontos
        defesa = 60 pontos

        posteriormente será adiconado classes que vão mudar os atributos
    """

    def __init__(self, name):
        super().__init__(70, 60, 60)
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"Herói: {self.__name} | Vida: {self.get_Life()} | Ataque: {self.get_Attack()} | Defesa: {self.get_Defense()}"
    
    def get_DisplayName(self):
        return f"Herói {self.get_name()}"
