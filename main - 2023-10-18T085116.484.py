# Sample coffee shop data with prices (you can replace this with real data)
coffee_shops = {
    "Coffee Shop A": 3.50,
    "Coffee Shop B": 4.00,
    "Coffee Shop C": 3.75,
    "Coffee Shop D": 3.25,
    "Coffee Shop E": 4.50,
}

# Function to find the cheapest coffee shop
def find_cheapest_coffee(coffee_shops):
    if not coffee_shops:
        return "No coffee shops found."

    cheapest_shop = min(coffee_shops, key=coffee_shops.get)
    cheapest_price = coffee_shops[cheapest_shop]

    return f"The cheapest coffee shop is '{cheapest_shop}' with a price of ${cheapest_price:.2f}."

# Call the function to find the cheapest coffee shop
cheapest_coffee = find_cheapest_coffee(coffee_shops)
print(cheapest_coffee)
