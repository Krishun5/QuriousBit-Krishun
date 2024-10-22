from product import ProductCatalog
from cart import Cart
from discount import DiscountManager
from currency import CurrencyConverter

def main():
    # Initialize the system components
    catalog = ProductCatalog()  # Manages product catalog
    cart = Cart()  # Manages the shopping cart
    discount_manager = DiscountManager()  # Handles discount logic
    currency_converter = CurrencyConverter()  # Handles currency conversion

    # Prepopulate the catalog with sample products
    catalog.add_product("P001", "Laptop", 1000.00, "Electronics")
    catalog.add_product("P002", "Phone", 500.00, "Electronics")
    catalog.add_product("P003", "T-Shirt", 20.00, "Fashion")

    # Command loop to process user input
    while True:
        command = input("> ").strip()  # Get user input
        if command == "exit":
            break  # Exit the program

        # Handle adding items to the cart
        if command.startswith("add_to_cart"):
            _, product_id, quantity = command.split()
            product = catalog.get_product(product_id)
            if product is None:
                print(f"Product {product_id} not found.")
            else:
                cart.add_item(product, int(quantity))  # Add product to the cart

        # View the current cart
        elif command == "view_cart":
            cart.view_cart()

        # List all available discounts
        elif command == "list_discounts":
            discount_manager.list_discounts()

        # Handle the checkout process, applying discounts and optional currency conversion
        elif command.startswith("checkout"):
            total_before_discount = cart.calculate_total()  # Calculate total before discounts
            print("Applying discounts...")  # Indicate that discounts are being applied

            discount_total = discount_manager.apply_discounts(cart)  # Apply discounts
            final_total = total_before_discount - discount_total  # Calculate the final total

            # Display the final total
            print(f"Final Total in USD: {final_total:.2f}")

            # Offer currency conversion to the user
            convert_currency = input("Would you like to view it in a different currency? (yes/no): ").strip()
            if convert_currency.lower() == "yes":
                currency = input("Enter currency (EUR/GBP): ").strip()
                final_converted = currency_converter.convert_currency(final_total, currency)
                print(f"Final Total in {currency}: {final_converted:.2f}")

        # Clear the cart
        elif command == "clear_cart":
            cart.clear_cart()

if __name__ == "__main__":
    main()
