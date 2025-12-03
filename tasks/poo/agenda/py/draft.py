class Fone:
<<<<<<< HEAD
    def __init__(self, id: str, number: str):
<<<<<<< HEAD
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
=======
=======
    def _init_(self, id: str, number: str):
>>>>>>> 80517d8863dba1f63ee09bb95e4ec8d3e112ede9
        self.__id = id
        self.__number = number
    
    def getId(self) -> str:
        return self.__id
    
    def getNumber(self) -> str:
        return self.__number

    def isValid(self) -> bool:
        validos: str = "0123456789()."
        
        for i in self.__number:
            if i not in validos:
                return False
        return True
    
    def _str_(self):
        return f"{self.getId()}:{self.getNumber()}"

class Contact:
    def _init_(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favorited: bool = False

    def getName(self):
        return self.__name
    
    def getFones(self):
        return self.__fones
    
    def setName(self, name: str):
        self.getName() == name
    
    def addFone(self, id: str, number: str):
        fone = Fone(id, number)

        if fone.isValid() == False:
            print("fail: invalid number")
            return
        
        self.__fones.append(fone)
    
    def rmFone(self, index: int):
        self.__fones.pop(index)
    
    def toogleFavorito(self):
        self._favorited = not self._favorited
    
    def isFavorited(self):
        return self.__favorited
    
    def _str_(self):
        fones = ", ".join([str(x) for x in self.__fones])
        return f"{"-" if self._favorited == False else "@"} {self._name} [{fones}]"

def main():
    contato = Contact("")

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(contato)
        elif args[0] == "init":
            contato = Contact(args[1])
        elif args[0] == "add":
            contato.addFone(args[1], args[2])
        elif args[0] == "rm":
            contato.rmFone(int(args[1]))
        elif args[0] == "tfav":
            contato.toogleFavorito()
        

<<<<<<< HEAD
main()

>>>>>>> 7de7ab832ae8d3b2d90fc4eda655fbf92ff77e24
=======
main()
>>>>>>> 80517d8863dba1f63ee09bb95e4ec8d3e112ede9
