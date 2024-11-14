from Dessert import Dessert


class Biscuit(Dessert):
    def __init__(self, name="", weight_kg=0.00, price_per_kg=0.00, type=""):
        super().__init__(name, weight_kg, price_per_kg)
        self.type = type
