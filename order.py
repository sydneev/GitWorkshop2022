class Order:
    def __init__(self):
        self.total_cost = 0
        self.items = []

    def add_frosted_lemonade(self):
        self.total_cost += 33
        self.items += ["frosted lemonade"]
        print("You have added frosted lemonade")

    def print_order(self):
        print('Your total is ${}'.format(self.total_cost))

        print('Here are your items: ', end = '')
        print(*self.items, sep = ', ')


    # implement methods for menu items
