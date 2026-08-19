asset_costs = [125.50, 999.99, 450.75, 1200.00, 75.25, 850.40]


asset_costs.sort(reverse=True)


print("Top 3 priciest assets:")

for price in asset_costs[:3]:
    print(price)
