class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def getId(self):
        return self.__id 

    def getNumber(self):
        return self.__number

    def isValid(self) -> bool:
        validos: str = "012345678()."

        for i in self.__number:
            if i not in validos:
                return False
        return True

    def __str__(self):
        return f"{self.__id}:{self.__number}"

class Contato:
    def __init__(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favoritado: bool = False
    
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
    
    def toogleFavorite(self):
        self.__favoritado = not self.__favoritado

    def isFavorited(self) -> bool:
        return self.__favoritado
    
    def __str__(self):
        fones = ", ".join([str(x) for x in self.__fones])
        return f"{"-" if self.__favoritado == False else "@"} {self.__name} [{fones}]"
    
class Agenda:
    def __init__(self):
        self.contatos: list[Contato] = []
    
    def findPosByName(self, name: str):
        for i, contato in enumerate(self.contatos):
            if contato.getName() == name:
                return i
        return -1
    
    def addContato(self, name: str, fones: list[Fone]):
        if self.findPosByName(name) == -1:
            novo_contato = Contato(name)
            for i in fones:
                novo_contato.addFone(i.getId(), i.getNumber())
            self.contatos.append(novo_contato)
        else:
            contato_existente = self.findPosByName(name)
            for i in fones:
                contato_existente.addFone(i.getId(), i.getNumber())
    
    def getContato(self, name: str) -> Contato | None:
        if self.findPosByName(name) != -1:
            return self.contatos[self.findPosByName(name)]
        
        return None

    def __str__(self):
        contatos = "\n".join([str(x) for x in self.contatos])
        return f"{contatos}"
    


def main():
    agenda = Agenda()

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(agenda)
        elif args[0] == "add":
            name = args[1]
            fones = []
            for item in args[2:]:
                id, number = item.split(":", 1)
                fones.append(Fone(id, number))
            agenda.addContato(name, fones)



main()
