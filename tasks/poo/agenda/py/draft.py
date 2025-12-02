class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id 
        self.__number = number
    
    def getId(self):
        return self.__id
    def getNumber(self):
        return self.__number
    def __str__(self):
        return f"{self.getId()}:{self.getNumber()}"


class Contato: 
    def __init__(self, nome: str, tel):
