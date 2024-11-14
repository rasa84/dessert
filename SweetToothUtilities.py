import os

from tabulate import tabulate

from Biscuit import Biscuit
from Chocolate import Chocolate
from Sweet import Sweet
from SweetTooth import SweetTooth


class SweetToothUtilities:
    DATA_DIRECTORY_NAME = 'data'
    DATA_DIRECTORY_PATH = "./" + DATA_DIRECTORY_NAME + "/"
    DESSERT_CLASSES = {
        "Šokoladai": Chocolate,
        "Sausainiai": Biscuit,
        "Saldainiai": Sweet
    }

    @staticmethod
    def print_sweet_tooth_with_most_expenses():
        sweet_teeth = SweetToothUtilities.create_sweet_teeth_from_files()
        max_cost_swt_tooth = sweet_teeth[0]
        for s in sweet_teeth:
            if s.calculate_total_cost() > max_cost_swt_tooth.calculate_total_cost():
                max_cost_swt_tooth = s
        print(
            f"Daugiausiai pinigų išleido: {max_cost_swt_tooth.name}. Jis/ji išleido: {max_cost_swt_tooth.calculate_total_cost()}")

    @staticmethod
    def print_most_expensive_sweets():
        swt_teeth = SweetToothUtilities.create_sweet_teeth_from_files()
        swt_tooth_with_m_exp_dessert = max(swt_teeth, key=lambda s: s.find_most_expensive_desserts()[0].price_per_kg)

        for swt_tooth in swt_teeth:
            dessert_info = [f"Pavadinimas: {d.name}, kaina: {d.price_per_kg}." for d in
                            swt_tooth.find_most_expensive_desserts()]
            # print(f"Smagurio vardas: {swt_tooth.name}. Jo/jos brangiausi saldumynai: {dessert_info}")

            swt_tooth_d_price = swt_tooth.find_most_expensive_desserts()[0].price_per_kg
            swt_tooth_with_m_exp_d_price = swt_tooth_with_m_exp_dessert.find_most_expensive_desserts()[0].price_per_kg
            if swt_tooth_d_price == swt_tooth_with_m_exp_d_price:
                print(
                    f"Smaguris pirkęs iš visų brangiausius saldumynus: {swt_tooth.name}. Jo/jos brangiausi saldumynai: {dessert_info}")

    @staticmethod
    def print_changed_first_sweet_tooth(name, money, age):
        swt_tooth = SweetToothUtilities.create_sweet_tooth_from_file("sweet_tooth1.txt")
        print(
            f"\nPradiniai smagurio duomenys\nvardas: {swt_tooth.name}, turi pinigų: {swt_tooth.money}, amžius {swt_tooth.age}")
        swt_tooth.name = name
        swt_tooth.money = money
        swt_tooth.age = age
        print(
            f"Pakeisti smagurio duomenys\nvardas: {swt_tooth.name}, turi pinigų: {swt_tooth.money}, amžius {swt_tooth.age}")

    @staticmethod
    def print_sorted_desserts(by):
        swt_teeth = SweetToothUtilities.create_sweet_teeth_from_files()
        for swt_tooth in swt_teeth:
            swt_tooth.sort_desserts(by)
            swt_tooth.print()

    @staticmethod
    def create_sweet_teeth_from_files():
        sweet_teeth = []
        with os.scandir(SweetToothUtilities.DATA_DIRECTORY_NAME) as dir:
            for file in dir:
                if file.name.endswith(".txt") and file.is_file():
                    swt_tooth = SweetToothUtilities.create_sweet_tooth_from_file(file.name)
                    sweet_teeth.append(swt_tooth)
        return sweet_teeth

    @staticmethod
    def create_sweet_tooth_from_file(file_name):
        with open(SweetToothUtilities.DATA_DIRECTORY_PATH + file_name, encoding='utf8') as file:
            swt_tooth_fields = SweetToothUtilities.get_split_row_fields(file.readline())
            sweet_tooth = SweetTooth(swt_tooth_fields[2], swt_tooth_fields[0], swt_tooth_fields[1])
            for row in file:
                dessert = SweetToothUtilities.create_dessert_from_file(row)
                sweet_tooth.add_dessert(dessert)
            return sweet_tooth

    @staticmethod
    def create_dessert_from_file(row):
        d_type, name, weight_kg, price_per_kg, additional_field = SweetToothUtilities.get_split_row_fields(row)
        dessert_class = SweetToothUtilities.DESSERT_CLASSES.get(d_type)
        if dessert_class is None:
            raise ValueError(f"Unknown type: {d_type}")
        return dessert_class(name, float(weight_kg), float(price_per_kg), additional_field)

    @staticmethod
    def get_split_row_fields(row):
        return row.rstrip('\n').split(',')
