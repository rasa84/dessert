from tabulate import tabulate


class SweetTooth:
    def __init__(self, money=0.00, name="", age=0):
        self.__money = money
        self.__name = name
        self.__age = age
        self.__desserts = []

    def add_dessert(self, dessert):
        self.__desserts.append(dessert)

    def get_desserts(self):
        return self.__desserts

    def find_most_expensive_desserts(self):
        max_price = max([dessert.price_per_kg for dessert in self.__desserts])
        # max_price_dessert = max(self.__desserts, key=lambda sweet: sweet.price_per_kg)
        return [dessert for dessert in self.__desserts if dessert.price_per_kg == max_price]

    def find_highest_cost_desserts(self):
        highest_cost = max([dessert.total_cost() for dessert in self.__desserts])
        return [dessert for dessert in self.__desserts if dessert.total_cost() == highest_cost]

    def calculate_total_cost(self):
        return sum([dessert.total_cost() for dessert in self.__desserts])

    def print(self):
        print(f"\nSmaguris: {self.name}")
        table = []
        for d in self.desserts:
            # print(f"\t - {d.name}. Kaina: {d.price_per_kg}")
            table.append([d.name, d.weight_kg, d.price_per_kg])
        print(tabulate(table, headers=["Pavadinimas", "Svoris (kg)", "Kaina / 1 kg"], tablefmt="pretty",
                       colalign=("left", "right", "right")))

    def sort_desserts(self, by='price_per_kg', reverse=False):
        if by == 'price_per_kg':
            self.__desserts.sort(key=lambda dessert: dessert.price_per_kg, reverse=reverse)
        elif by == 'name':
            self.__desserts.sort(key=lambda dessert: dessert.name, reverse=reverse)
        return self.__desserts

    @property
    def money(self):
        return self.__money

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def desserts(self):
        return self.__desserts

    @money.setter
    def money(self, money):
        self.__money = money

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age
