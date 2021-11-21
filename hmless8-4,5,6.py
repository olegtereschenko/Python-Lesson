
class Equipment:

    def __init__(self,model,color,paper,price):
        self._model = model
        self._color = color
        self._paper = paper
        self._price = price

    @property
    def model(self):
        return self._model


class Printer(Equipment):

    def __init__(self, model, color,paper,dpi):
        self.type = type
        super().__init__(model, color,paper,dpi)


class Copy(Equipment):

    def __init__(self, model, color, paper,dpi, printspeed, maxpaper):
        self.printspeed = printspeed
        self.maxpaper = maxpaper
        super().__init__(model, color, paper, dpi,printspeed, maxpaper)

class Scanner(Equipment):
    
