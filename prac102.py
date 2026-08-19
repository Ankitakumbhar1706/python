product_labels = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]

item_name = input("Enter the product name to search: ").lower()

if item_name in product_labels:
    index = product_labels.index(item_name)
    print("Item found!")
    print("Index location:", index)
else:
    print("Item not found in the inventory.")
