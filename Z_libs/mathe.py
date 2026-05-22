import math
import functions

class mathe:
    def __init__(self):
        self._functions = functions.functions(False)

    def pi(self):
        return math.pi
    
    def sin(self, x):
        try:
            x = float(x)
        except ValueError:
            self._functions.ausgabe("Fehler", "r")
            print("Bitte eine gültige Zahl übergeben")
            return
        x = math.radians(x)
        y = math.sin(x)
        y = round(y, 10)
        if y % 1 == 0: y = int(y)
        return y
    
    def cos(self, x):
        try:
            x = float(x)
        except ValueError:
            self._functions.ausgabe("Fehler", "r")
            print("Bitte eine gültige Zahl übergeben")
            return
        x = math.radians(x)
        y = math.cos(x)
        y = round(y, 10)
        if y % 1 == 0: y = int(y)
        return y
    
    # √
    def wurzel(self, x, We = 2):
        try:
            x = float(x)
            We = float(We)
        except ValueError:
            self._functions.ausgabe("Fehler", "r")
            print("Bitte eine gültige Zahl übergeben")
            return
        y = x ** (1 / We)
        if y % 1 == 0: y = int(y)
        return y