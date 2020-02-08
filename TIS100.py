# TIS-100.py
from copy import deepcopy


class Console:
    def __init__(self):
        """
        Console or Node is the fundamental reprogrammable
        unit of TIS-100.
        """
        self.ACC = 0
        self.BAK = 0
        self.UP = 1
        self.DOWN = 0
        self.LEFT = 0
        self.RIGHT = 0

        self.IN = 0
        self.OUT = 0
        self.translations = {
            "up": self.UP,
            "down": self.DOWN,
            "left": self.LEFT,
            "right": self.RIGHT,
            "acc": self.ACC,
            "bak": self.BAK,
        }

    def updateT(self):
        """
        Updates the translation dictionary
        wrt to the console variables.
        """
        self.translations = {
            "up": self.UP,
            "down": self.DOWN,
            "left": self.LEFT,
            "right": self.RIGHT,
            "acc": self.ACC,
            "bak": self.BAK,
        }

    def updateV(self):

        self.UP = self.translations["up"]
        self.DOWN = self.translations["down"]
        self.LEFT = self.translations["left"]
        self.RIGHT = self.translations["right"]
        self.ACC = self.translations["acc"]
        self.BAK = self.translations["bak"]

    def mov(self, src, dst):
        if src in self.translations.keys() and dst in self.translations.keys():
            self.translations[dst] = deepcopy(self.translations[src])
            self.translations[src] = 0
            src = None
        else:
            print("[MOV] Error")
        self.updateV()
        self.updateT()

    def swp(self):
        self.BAK, self.ACC = self.ACC, self.BAK
        self.updateT()

    def sav(self):
        self.BAK = deepcopy(self.ACC)
        self.updateT()

    def add(self, num):
        if type(num) is int:
            self.ACC += num
        else:
            self.ACC += self.translations[num]
        self.updateT()

    def sub(self, num):
        if type(num) is int:
            self.ACC -= num
        else:
            self.ACC -= self.translations[num]
        self.updateT()

    def neg(self):
        self.ACC *= -1
        self.updateT()

    def nop(self):
        pass

    def __str__(self):
        return f"ACC: {self.ACC}\nBAK: {self.BAK}\n----------"


if __name__ == "__main__":
    c = Console()
    c.ACC = 2
    c.add("up")
    c.mov("up", "acc")
    print(c)
