# Creating Brunch, Early Bird, Dinner and Kids menus
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        str_repr = f"{self.name} menu is available from {self.start_time} to {self.end_time}"
        return str_repr
    
    def calculate_bill(self, purchased_items):
        total_price = 0
        for item in purchased_items:
            total_price += self.items[item]
        return total_price
    



# Brunch Menu
brunch_items = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, git 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}
brunch = Menu('Brunch', brunch_items, 11, 16)

# Early Bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50,
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu('Early Bird', early_bird_items, 15, 18)

# Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 
  'caesar salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
}
dinner = Menu('Dinner', dinner_items, 17, 23)

# Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}
kids = Menu('Kids', kids_items, 11, 21)
#---------------------------------------------------#

# Test repr for created objects
# print(brunch)
# print(early_bird)
# print(dinner)
# print(kids)



# Test calculate() method
def print_receipt(orders, total):
    print("\n************* RECEIPT *******************")
    for order in orders:
        print(f"{order}")
    print(f"\nTotal {total}")
    print("******************************************\n")

breakfast_order = ['pancakes', 'home fries', 'coffee']
breakfast_order__total = brunch.calculate_bill(breakfast_order)
print_receipt(breakfast_order, breakfast_order__total)

# early bird order
early_bird_order = ['salumeria plate']
dinner_order = [ 'mushroom ravioli (vegan)']
early_bird_dinner_total = dinner.calculate_bill(dinner_order) + early_bird.calculate_bill(early_bird_order)
print_receipt(early_bird_order + dinner_order, early_bird_dinner_total)