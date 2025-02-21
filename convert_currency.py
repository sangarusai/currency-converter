from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    # Create an object of the CurrencyRates class
    cr = CurrencyRates()

    # Get the exchange rate
    try:
        rate = cr.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        return converted_amount
    except Exception as e:
        return f"Error: {e}"

# Example usage
amount = float(input("Enter amount to convert: "))
from_currency = input("Enter currency to convert from (e.g., USD): ").upper()
to_currency = input("Enter currency to convert to (e.g., EUR): ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
