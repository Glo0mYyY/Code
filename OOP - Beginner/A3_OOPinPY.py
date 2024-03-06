class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        item_details = {
            'item_name': item_name,
            'stock_count': stock_count,
            'price': price
        }
        self.items[item_id] = item_details

    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.items:
            item_details = self.items[item_id]
            if item_name:
                item_details['item_name'] = item_name
            if stock_count:
                item_details['stock_count'] = stock_count
            if price:
                item_details['price'] = price
        else:
            print(f"Item with ID {item_id} does not exist.")

    def check_item_details(self, item_id):
        if item_id in self.items:
            return self.items[item_id]
        else:
            print(f"Item with ID {item_id} does not exist.")

inv = Inventory()
inv.add_item(1, "Laptop", 100, 500)
print (inv.check_item_details(1))
inv.update_item(1, item_name="Laptop", stock_count=150, price=600)
print (inv.check_item_details(1))