# Represents an individual product in the catalog
class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

# Manages the entire product catalog
class ProductCatalog:
    def __init__(self):
        self.products = {}

    # Add a new product to the catalog
    def add_product(self, product_id, name, price, category):
        product = Product(product_id, name, price, category)
        self.products[product_id] = product

    # Fetch a product by its ID
    def get_product(self, product_id):
        return self.products.get(product_id, None)

    # List all products in the catalog (for debugging or display purposes)
    def list_products(self):
        for product in self.products.values():
            print(f"{product.product_id}: {product.name}, Price: {product.price} USD, Category: {product.category}")
