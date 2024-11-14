from Dessert import Dessert


class Chocolate(Dessert):
    def __init__(self, name="", weight_kg=0.00, price_per_kg=0.00, cocoa_percentage=50):
        super().__init__(name, weight_kg, price_per_kg)
        self.cocoa_percentage = cocoa_percentage
