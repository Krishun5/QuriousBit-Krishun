# Manages the currency conversion logic
class CurrencyConverter:
    def __init__(self):
        # Fixed conversion rates for supported currencies
        self.rates = {
            "EUR": 0.85,
            "GBP": 0.75
        }

    # Convert an amount in USD to the desired currency
    def convert_currency(self, amount, currency):
        if currency in self.rates:
            return amount * self.rates[currency]
        else:
            print(f"Currency {currency} not supported.")
            return amount
