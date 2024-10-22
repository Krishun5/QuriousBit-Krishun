class Cart:
    def __init__(self):
        self.items = {}

    # Add a product to the cart, supports multiple quantities
    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}

        # Confirmation message when an item is added
        print(f"{quantity} {product.name}(s) added to the cart.")  # This line should print now
    
    # Display the current cart contents along with total prices
    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        total = 0
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            item_total = product.price * quantity
            total += item_total
            print(f"{product.name} - Quantity: {quantity}, Price: {product.price:.2f} USD, Total: {item_total:.2f} USD")
        print(f"Total (before discounts): {total:.2f} USD")

    # Calculate the total cost of the cart before any discounts
    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    # Clear all items from the cart
    def clear_cart(self):
        self.items = {}
        print("Your cart has been cleared.")
