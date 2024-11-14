class Dessert:
    def __init__(self, name="", weight_kg=0.00, price_per_kg=0.00):
        self.name = name
        self.weight_kg = weight_kg
        self.price_per_kg = price_per_kg

    def total_cost(self):
        return self.weight_kg * self.price_per_kg
