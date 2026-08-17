print("===== CONSUMER TRANSACTION TRACKER =====")

transactions = []


for i in range(5):
    amount = float(input(f"Enter transaction {i + 1}: "))
    transactions.append(amount)


largest = max(transactions)


average = sum(transactions) / len(transactions)


print("\n===== TRANSACTION SUMMARY =====")
print("Transactions:", transactions)
print("Largest Transaction: ", largest)
print("Average Spend: ", average)