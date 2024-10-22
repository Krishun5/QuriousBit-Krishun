# Mini E-commerce Cart System

## Overview
This command-line application allows users to manage a shopping cart. The key features include:
- Adding/removing items to/from the cart.
- Viewing the cart's contents and total cost.
- Automatic application of available discounts at checkout.
- Currency conversion of the final total price.

## Features
- **Product Management**: A catalog of preloaded products (Laptop, Phone, T-Shirt).
- **Cart Operations**: Users can add products, view the cart, and proceed to checkout.
- **Discounts**: Supports Buy 1 Get 1 Free for fashion items, and 10% off on electronics.
- **Currency Conversion**: Convert the final total to EUR or GBP.

## Assumptions
- All prices are stored in USD.
- Fixed conversion rates are used for currency conversion.

## How to Run
1. Run **main.py** in a Python environment.
2. Use commands like 

**add_to_cart <product_id> <quantity>**(the command will add products to your cart), 
**view_cart**(you can view your cart and your toal amount to be paid), 
**list_discounts**(to get details of all the discounts),and 
**checkout**(checkout call will help to automatically apply  discounts and give your total to be paid amount in USD . Checkout call will also help the customers to pay in diffrent currencies like in EUR , GBP),
**clear_cart**(this command will help to clear the cart for new customers)
to interact with the system.
