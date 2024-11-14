from Biscuit import Biscuit
from Chocolate import Chocolate
from Sweet import Sweet
from SweetTooth import SweetTooth
from SweetToothUtilities import SweetToothUtilities

# chocolate1 = Chocolate("Karališkas", 0.5, 6.00, 50)
# chocolate2 = Chocolate("Juodasis", 0.5, 4.50, 70)
# biscuit = Biscuit("Trapukai", 2.2, 6, "traškūs")
# sweet = Sweet("Gaidelis", 10.2, 4, "šokoladiniai")
#
# sweet_tooth = SweetTooth(30, "Juozas", 21)
# sweet_tooth.add_dessert(chocolate1)
# sweet_tooth.add_dessert(chocolate2)
# sweet_tooth.add_dessert(biscuit)
# sweet_tooth.add_dessert(sweet)
#
# print(
#     f"Brangiausi saldumynai: {[dessert.name + " - " + str(dessert.price_per_kg) for dessert in sweet_tooth.find_most_expensive_desserts()]}")
# print(
#     f"Daugiausiai pinigų išleis: {[dessert.name + " - " + str(dessert.total_cost()) for dessert in sweet_tooth.find_highest_cost_desserts()]}")

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

SweetToothUtilities.print_sweet_tooth_with_most_expenses()
SweetToothUtilities.print_most_expensive_sweets()
SweetToothUtilities.print_sorted_desserts('name')
SweetToothUtilities.print_changed_first_sweet_tooth("Petriukas", 280, 36)
