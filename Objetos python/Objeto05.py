class Terreno(object):
    def __init__(self, width: float, height: float, cost: float ):
        self.width = width
        self.height = height
        self.cost = cost
 
    def perimetro(self) -> float:
        return 2*(self.width + self.height)
 
    def area(self) -> float:
        return self.cost * self.width
 
    def precio(self) -> float:
        return self.area() * self.cost
 
    def __str__(self):
        return f"{​​​​​​self.__class__.__name__}​​​​​​({​​​​​​self.width}​​​​​​, {​​​​​​self.height}​​​​​​, {​​​​​​self.cost}​​​​​​)"
 

instance = Terreno(10, 20, 3)
print(instance)