from Dessert import Dessert


class Sweet(Dessert):
    def __init__(self, name="", weight_kg=0.00, price_per_kg=0.00, flavor=""):
        super().__init__(name, weight_kg, price_per_kg)
        self.flavor = flavor
