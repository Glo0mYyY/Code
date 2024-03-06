class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item):
        self.menu_items.append(item)

    def book_tables(self, table):
        self.book_table.append(table)

    def customer_order(self, order):
        self.customer_orders.append(order)

    def print_menu(self):
        print("Menu Items:")
        for item in self.menu_items:
            print(item)

    def print_booked_tables(self):
        print("Booked Tables:")
        for table in self.book_table:
            print(table)

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(order)


# Create an instance of the Restaurant class
restaurant = Restaurant()

# Add items to the menu
restaurant.add_item_to_menu("Pasta")
restaurant.add_item_to_menu("Steak")
restaurant.add_item_to_menu("Fish")

# Book tables
restaurant.book_tables("Table 4")
restaurant.book_tables("Table 5")
restaurant.book_tables("Table 6")

# Take customer orders
restaurant.customer_order("Pasta")
restaurant.customer_order("Steak")
restaurant.customer_order("Fish")

# Print the menu
restaurant.print_menu()

# Print booked tables
restaurant.print_booked_tables()

# Print customer orders
restaurant.print_customer_orders()
