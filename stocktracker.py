stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 140,
    "MSFT": 320
}

portfolio = {}

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", ', '.join(stock_prices.keys()))
print("Type 'done' when finished.\n")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in price list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Invalid quantity. Must be a number.")

print("\n=== Portfolio Summary ===")
total_value = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")

save_option = input("Do you want to save this summary to a file? (yes/no): ").lower()
if save_option == "yes":
    filename = input("Enter filename (with .txt or .csv extension): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock},{qty},{price},{value}\n")
        file.write(f"\nTotal Investment Value,,,{total_value}\n")
    print(f"Portfolio saved to {filename}")
