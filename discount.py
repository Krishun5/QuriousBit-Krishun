class DiscountManager:
    def __init__(self):
        # Define available discounts with categories and functions
        self.discounts = {
            "Fashion": {"type": "Buy 1 Get 1 Free", "function": self.buy_one_get_one_free},
            "Electronics": {"type": "10% Off", "function": self.ten_percent_off}
        }

    # Display all available discounts
    def list_discounts(self):
        print("Available Discounts:")
        for category, details in self.discounts.items():
            print(f"{details['type']} on {category} items")

    # Apply discounts to the cart and return the total discount amount
    def apply_discounts(self, cart):
        total_discount = 0
        for item in cart.items.values():
            category = item['product'].category
            if category in self.discounts:
                discount_function = self.discounts[category]["function"]
                discount_amount = discount_function(item)
                if discount_amount > 0:
                    print(f"{self.discounts[category]['type']} on {item['product'].name} applied.")
                    total_discount += discount_amount
        return total_discount

    # Buy 1 Get 1 Free for fashion items
    def buy_one_get_one_free(self, item):
        if item['quantity'] >= 2:
            discount_amount = (item['quantity'] // 2) * item['product'].price
            return discount_amount
        return 0

    # 10% discount on electronics
    def ten_percent_off(self, item):
        discount_amount = item['product'].price * item['quantity'] * 0.1
        return discount_amount


